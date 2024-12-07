package actions

import (
	"log"
	"opengo/configuration"
	"opengo/datapoints"
)

type ActionGroup struct {
	logger     *log.Logger
	config     *configuration.ActionsConfig
	datapoints *datapoints.DataPointCollection
	channel    chan datapoints.DataPointId
	stopped    bool
}

func NewActionGroup(logger *log.Logger, config *configuration.ActionsConfig, datapoints *datapoints.DataPointCollection, channel chan datapoints.DataPointId) ActionGroup {
	return ActionGroup{logger: logger, config: config, datapoints: datapoints, channel: channel, stopped: false}
}

func (ag *ActionGroup) Start() {
	ag.logger.Println("Starting action group")
	ag.logger.Printf("Actions configuration %f\n", *ag.config)

	for msg := range ag.channel {
		ag.logger.Println("Channel message (in actions): ", msg)
		// time.Sleep(1.00 * time.Second)
	}
}

func (ag *ActionGroup) Stop() {
	ag.logger.Println("Stopping action group")
	ag.stopped = true
}
