package main

import (
	"log"
	"opengo/actions"
	"opengo/configuration"
	"opengo/datapoints"
	"opengo/intakes"
	"os"
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

	// (TODO) There may be some web server initialization at this point

	// (TODO) There may ne some REST API router initialization at this point

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
