package intakes

import (
	"log"
	"opengo/configuration"
	"opengo/datapoints"
	"time"
)

type DataIntake struct {
	logger     *log.Logger
	config     *configuration.IntakeConfig
	datapoints *datapoints.DataPointCollection
	channel    chan datapoints.DataPointId
	stopped    bool
}

func NewDataIntake(logger *log.Logger, config *configuration.IntakeConfig, datapoints *datapoints.DataPointCollection, channel chan datapoints.DataPointId) DataIntake {
	return DataIntake{logger: logger, config: config, datapoints: datapoints, channel: channel, stopped: false}
}

func (di *DataIntake) Start() {
	di.logger.Println("Starting data intake")
	di.logger.Printf("Data intake configuration %f\n", *di.config)

	intakeRate := di.config.IntakeRateHz
	if intakeRate <= 0 {
		intakeRate = 1.0
	}

	for !di.stopped {
		di.logger.Println("Data intake running...")
		for _, dp := range di.datapoints.DataPoints {
			di.UpdateDataPoint(&dp)
		}
		time.Sleep(time.Duration(1/intakeRate) * time.Second)
	}

}

func (di *DataIntake) Stop() {
	di.logger.Println("Stopping data intake")
	di.stopped = true
}

func (di *DataIntake) UpdateDataPoint(dp *datapoints.DataPoint) {

	// For now using some random value; in the future this comes from the sensor
	dp.UpdateValue(1.0 + float64(time.Now().Nanosecond()%100)/100.0)
	di.Emit(dp)
}

func (di *DataIntake) Emit(dp *datapoints.DataPoint) {
	di.channel <- dp.Id
}
