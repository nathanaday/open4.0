<template>
    <div id="point-cloud-container" style="width: 100%; height: 100vh;"></div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';
import { GUI } from 'dat.gui'; // Named import
import * as dat from 'dat.gui'; // Full namespace import
import ColorMap from '../assets/cmaps.js';

export default {
    name: 'PointCloudDemo',
    data() {
        return {
            gui: new GUI(),
            settings: {
                pointSize: 0.1,
                color: '#DE3163',
                colorMap: ['viridis', 'magma', 'inferno', 'plasma'],
                wireframeOpacity: 0.4,

            },
            material: null,
            pointCloud: null,

            colorMap: new ColorMap(),
            colorMapOptions: ['viridis', 'magma', 'inferno', 'plasma'],
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

            // this.material = new THREE.PointsMaterial({
            //     color: 0xDE3163,
            //     size: 0.05,
            //     sizeAttenuation: true,
            //     vertexColors: true
            // });

            // this.material = new THREE.MeshPhysicalMaterial({
            //     color: 0xDE3163,
            //     // envMap: envTexture,
            //     metalness: 0,
            //     roughness: 0,
            //     transparent: false,
            //     transmission: 0.2,
            //     side: THREE.DoubleSide,
            //     clearcoat: 1.0,
            //     clearcoatRoughness: 0.25,
            //     vertexColors: true
            // });

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

                    // const surfaceMesh = new THREE.Mesh(geometry, surfaceMaterial);
                    // scene.add(surfaceMesh);

                    const wireframeMesh = new THREE.Mesh(geometry, wireframeMaterial);
                    scene.add(wireframeMesh);

                    // const pointCloud = new THREE.Mesh(geometry, this.material);
                    // mesh.rotateX(-Math.PI / 2);

                    // const pointCloud = new THREE.Points(geometry, this.material);

                    geometry.setAttribute('color', new THREE.BufferAttribute(new Float32Array(geometry.attributes.position.count * 3), 3));
                    this.createGradient(geometry);

                    // pointCloud.rotateX(-Math.PI / 2);
                    // scene.add(pointCloud);
                    this.pointCloud = wireframeMesh;
                },
                (xhr) => {
                    console.log((xhr.loaded / xhr.total) * 100 + '% loaded')
                },
                (error) => {
                    console.log(error)
                }
            )

            // Generate points
            // const geometry = new THREE.BufferGeometry();
            // const vertices = [];
            // for (let i = 0; i < 10000; i++) {
            //     const x = THREE.MathUtils.randFloatSpread(2000);
            //     const y = THREE.MathUtils.randFloatSpread(2000);
            //     const z = THREE.MathUtils.randFloatSpread(2000);
            //     vertices.push(x, y, z);
            // }
            // geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));

            // Define shaders and uniforms
            // const uniforms = {
            //     pointSize: { value: this.settings.pointSize },
            //     color: { value: new THREE.Color(this.settings.color) },
            //     intensityC: { value: this.settings.intensityC },
            //     intensityP: { value: this.settings.intensityP },
            //     viewVector: { value: camera.position }
            // };



            // const pointCloud = new THREE.Points(geometry, this.material);
            // const pointCloud = new THREE.Points(geometry);
            // scene.add(pointCloud);
            // scene.fog = new THREE.Fog(0x000000, 1, 500);  // 4068# 6347#

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

            // this.gui.addColor(this.settings, 'color').onChange(value => {
            //     // uniforms.color.value.setStyle(value);
            //     this.material.color.set(value);
            // });


            this.gui.add(this.settings, 'wireframeOpacity', 0, 1).onChange(value => {
                // uniforms.color.value.setStyle(value);
                this.material.opacity = value;
            });

            // Add a control to select color map from options: viridis, magma, inferno, plasma
            this.gui.add(this.settings, 'colorMap', this.colorMapOptions).onChange(value => {

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
                // const color = startColor.clone().lerp(endColor, t); // Interpolate between startColor and endColor

                // // Find the two nearest stops
                // let lowerStop = gradientStops[0];
                // let upperStop = gradientStops[gradientStops.length - 1];
                // for (let j = 0; j < gradientStops.length - 1; j++) {
                //     if (t >= gradientStops[j].stop && t <= gradientStops[j + 1].stop) {
                //         lowerStop = gradientStops[j];
                //         upperStop = gradientStops[j + 1];
                //         break;
                //     }
                // }

                // // Calculate the local interpolation parameter
                // const localT = (t - lowerStop.stop) / (upperStop.stop - lowerStop.stop);
                // const color = lowerStop.color.clone().lerp(upperStop.color, localT); // Interpolate between the two nearest colors

                const colorMap = this.selectedColorMap;

                // console.log('Color map options', this.colorMapOptions)
                // console.log('Selected color map:', this.selectedColorMap);
                // console.log('Color map:', colorMap);

                const color = this.colorMap.getColorFromMap(t, colorMap);
                colors[i] = color.r;
                colors[i + 1] = color.g;
                colors[i + 2] = color.b;

            }
            geometry.attributes.color.needsUpdate = true;

        },

        // getColorFromMap(value, colorMap) {
        //     const index = value * (colorMap.length - 1);
        //     const lowerIndex = Math.floor(index);
        //     const upperIndex = Math.ceil(index);
        //     const ratio = index - lowerIndex;

        //     const lowerColor = colorMap[lowerIndex];
        //     const upperColor = colorMap[upperIndex] || colorMap[lowerIndex]; // Handle edge case

        //     const r = lowerColor[0] + ratio * (upperColor[0] - lowerColor[0]);
        //     const g = lowerColor[1] + ratio * (upperColor[1] - lowerColor[1]);
        //     const b = lowerColor[2] + ratio * (upperColor[2] - lowerColor[2]);

        //     return new THREE.Color(`rgb(${Math.round(r)}, ${Math.round(g)}, ${Math.round(b)})`);
        // }
    }
};
</script>

<style scoped></style>
