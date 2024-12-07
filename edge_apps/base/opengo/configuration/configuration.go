package configuration

import "opengo/datapoints"

type AppConfig struct {
	IntakeConfig      IntakeConfig      `json:"intakeConfig"`
	DatabaseConfig    DatabaseConfig    `json:"databaseConfig"`
	WebServerConfig   WebServerConfig   `json:"webServerConfig"`
	ApiConfig         ApiConfig         `json:"apiConfig"`
	ActionsConfig     ActionsConfig     `json:"actionsConfig"`
	PerformanceConfig PerformanceConfig `json:"performanceConfig"`
}

type IntakeConfig struct {
	IntakeRateHz float32
}

type DatabaseConfig struct {
	// (TODO) Add database configuration fields here
}

type WebServerConfig struct {
	// (TODO) Add web server configuration fields here
}

type ApiConfig struct {
	// (TODO) Add API configuration fields here
}

type ActionsConfig struct {
	// (TODO) Add actions configuration fields here
}

type PerformanceConfig struct {
	// (TODO) Add performance configuration fields here
}

func New() AppConfig {

	// (TODO) Load configuration from file or environment variables

	return AppConfig{
		IntakeConfig:      IntakeConfig{IntakeRateHz: 1.0},
		DatabaseConfig:    DatabaseConfig{},
		WebServerConfig:   WebServerConfig{},
		ApiConfig:         ApiConfig{},
		ActionsConfig:     ActionsConfig{},
		PerformanceConfig: PerformanceConfig{},
	}
}

func MakeDataPointCollection() datapoints.DataPointCollection {

	// (TODO) Load data points from configuration file or database
	dp1 := datapoints.DataPoint{Value: 1.0, Id: datapoints.DataPointId{IntId: 1, StrId: "dp1"}}
	dp2 := datapoints.DataPoint{Value: 2.0, Id: datapoints.DataPointId{IntId: 2, StrId: "dp2"}}
	dp3 := datapoints.DataPoint{Value: 3.0, Id: datapoints.DataPointId{IntId: 3, StrId: "dp3"}}

	dpc := datapoints.DataPointCollection{
		DataPoints: []datapoints.DataPoint{dp1, dp2, dp3},
	}

	return dpc
}
