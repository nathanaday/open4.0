package main

import (
	"log"
	"opengo/actions"
	"opengo/configuration"
	"opengo/datapoints"
	"opengo/image_processing"
	"opengo/intakes"
	"os"

	"github.com/gin-gonic/gin"
)

type application struct {
	config     configuration.AppConfig
	datapoints datapoints.DataPointCollection
}

func main() {

	logger := log.New(os.Stdout, "opengo: ", log.LstdFlags)
	logger.Println("Starting OpenGo")

	app := application{
		config:     configuration.New(),
		datapoints: configuration.MakeDataPointCollection(),
	}

	// Defining a channel for sharing data point collections
	//  A channel will send a datapoint collection when they touch or modify those datapoints
	//  This allows other services to realize some data has been updated
	c := make(chan datapoints.DataPointId)

	// (TODO) There may be some database initialization at this point
	// ...

	// REST API router initialization
	router := gin.Default()
	imageGroup := router.Group("/images")
	{
		imageGroup.POST("/inspect", image_processing.InspectImageHandler)
		imageGroup.POST("/analyze", image_processing.AnalyzeImageHandler)
		imageGroup.GET("/analysis_status", image_processing.AnalysisStatusHandler)
	}

	// Model management routes
	modelGroup := router.Group("/models")
	{
		modelGroup.GET("/manifest", image_processing.GetModelsManifestHandler)
		modelGroup.POST("/download", image_processing.RequestDownloadModelHandler)
		modelGroup.POST("/update", image_processing.RequestUpdateModelHandler)
		modelGroup.POST("/remove", image_processing.RequestRemoveModelHandler)
	}

	// Run the server
	go router.Run(":8080")

	// Starting the data intake process
	di := intakes.NewDataIntake(logger, &app.config.IntakeConfig, &app.datapoints, c)
	go di.Start()

	// Start the actions handler
	ag := actions.NewActionGroup(logger, &app.config.ActionsConfig, &app.datapoints, c)
	go ag.Start()

	// Main loop
	for msg := range c {
		log.Println("Channel message (in main): ", msg)
		// time.Sleep(1.00 * time.Second)
	}

}
