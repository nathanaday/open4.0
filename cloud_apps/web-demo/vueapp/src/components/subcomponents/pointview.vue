<template>
    <div id="point-cloud-container" style="width: 100%; height: 100vh;"></div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';
import { GUI } from 'dat.gui'; // Named import
import ColorMap from '../../assets/cmaps.js';

export default {
    name: 'PointView',
    data() {
        return {
            gui: new GUI(),
            settings: {
                pointSize: 0.1,
                color: '#DE3163',
                colorMapOptions: ['viridis', 'magma', 'inferno', 'plasma'],
                wireframeOpacity: 0.4,

            },
            material: null,
            pointCloud: null,

            colorMap: new ColorMap(),
            selectedColorMap: 'viridis'
        };
    },
    mounted() {
        this.initPointCloud();
    },
    beforeDestroy() {
        if (this.renderer) {
            this.container.removeChild(this.renderer.domElement);
            window.removeEventListener('resize', this.onWindowResize);
            this.renderer.dispose(); // Dispose the renderer
            this.gui.destroy(); // Remove the GUI
        }
    },
    methods: {
        initPointCloud() {

            this.container = document.getElementById('point-cloud-container');
            const scene = new THREE.Scene();
            scene.add(new THREE.AxesHelper(5))

            // const light = new THREE.SpotLight()
            const light = new THREE.DirectionalLight(0xffffff, 5);
            light.position.set(2000, 2000, 2000)
            scene.add(light)

            const camera = new THREE.PerspectiveCamera(75, this.container.offsetWidth / this.container.offsetHeight, 0.1, 1000);
            camera.position.z = 20;

            this.renderer = new THREE.WebGLRenderer();
            this.renderer.setSize(this.container.offsetWidth, this.container.offsetHeight);
            this.container.appendChild(this.renderer.domElement);

            const controls = new OrbitControls(camera, this.renderer.domElement);
            controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
            controls.dampingFactor = 0.25;
            controls.screenSpacePanning = false;
            controls.minDistance = 10;
            controls.maxDistance = 5000;
            controls.maxPolarAngle = Math.PI / 2;

            // Material for the semi-transparent surface
            const surfaceMaterial = new THREE.MeshStandardMaterial({
                color: 0xDE3163, // Adjust the color as needed
                metalness: 0.5,
                roughness: 0.5,
                transparent: true,
                opacity: 0.5, // Adjust for desired transparency level
                side: THREE.DoubleSide,
            });

            // Material for the wireframe
            const wireframeMaterial = new THREE.MeshBasicMaterial({
                color: 0xffffff, // Adjust the wireframe color as needed
                wireframe: true,
                transparent: true,
                opacity: 0.4, // Adjust to make the wireframe more or less pronounced
                vertexColors: true
            });

            this.material = wireframeMaterial;

            const loader = new PLYLoader();
            loader.load(
                'goatskull.ply',
                (geometry) => { // Changed to arrow function
                    geometry.computeVertexNormals();

                    const wireframeMesh = new THREE.Mesh(geometry, wireframeMaterial);
                    scene.add(wireframeMesh);

                    geometry.setAttribute('color', new THREE.BufferAttribute(new Float32Array(geometry.attributes.position.count * 3), 3));
                    this.createGradient(geometry);

                    this.pointCloud = wireframeMesh;
                },
                (xhr) => {
                    console.log((xhr.loaded / xhr.total) * 100 + '% loaded')
                },
                (error) => {
                    console.log(error)
                }
            )

            // Animation loop
            const animate = () => {
                requestAnimationFrame(animate);
                if (this.pointCloud) {
                    this.pointCloud.rotation.x += 0.0005;
                    this.pointCloud.rotation.y += 0.0005;
                }
                this.renderer.render(scene, camera);
            };
            animate();

            this.setupGUI();
            this.onWindowResize = () => {
                camera.aspect = this.container.offsetWidth / this.container.offsetHeight;
                camera.updateProjectionMatrix();
                this.renderer.setSize(this.container.offsetWidth, this.container.offsetHeight);
                controls.update();
            };
            window.addEventListener('resize', this.onWindowResize);
        },
        setupGUI() {
            this.gui.add(this.settings, 'pointSize', 0.01, 1).onChange(value => {
                // uniforms.pointSize.value = value;
                this.material.size = value;
            });

            this.gui.add(this.settings, 'wireframeOpacity', 0, 1).onChange(value => {
                // uniforms.color.value.setStyle(value);
                this.material.opacity = value;
            });

            // Add a control to select color map from options: viridis, magma, inferno, plasma
            this.gui.add(this.settings, 'colorMapOptions', ['viridis', 'magma', 'inferno', 'plasma']).onChange(value => {

                console.log('Selected color map:', value);

                this.selectedColorMap = value;
                this.createGradient(this.pointCloud.geometry);
            });
        },

        createGradient(geometry) {

            const gradientStops = [
                { stop: 0, color: new THREE.Color(0x0000ff) }, // Blue
                { stop: 0.5, color: new THREE.Color(0x00ff00) }, // Green
                { stop: 1, color: new THREE.Color(0xff0000) } // Red
            ];

            // const startColor = new THREE.Color(0x0000ff); // Blue
            // const endColor = new THREE.Color(0xff0000); // Red

            // Calculate min and max values of the property to base the gradient on (e.g., y-coordinate)
            let minVal = Infinity, maxVal = -Infinity;
            const positions = geometry.attributes.position.array;
            for (let i = 0; i < positions.length; i += 3) {
                const z = positions[i + 2];
                minVal = Math.min(minVal, z);
                maxVal = Math.max(maxVal, z);
            }

            // Apply colors based on y-coordinate
            const colors = geometry.attributes.color.array;
            for (let i = 0; i < positions.length; i += 3) {
                const y = positions[i + 1];
                const z = positions[i + 2];
                const t = (z - minVal) / (maxVal - minVal); // Normalize y to [0, 1]

                const colorMap = this.selectedColorMap;

                const color = this.colorMap.getColorFromMap(t, colorMap);
                colors[i] = color.r;
                colors[i + 1] = color.g;
                colors[i + 2] = color.b;

            }
            geometry.attributes.color.needsUpdate = true;

        },

    }
};
</script>

<style scoped></style>
