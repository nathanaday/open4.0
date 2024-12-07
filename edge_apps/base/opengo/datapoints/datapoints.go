package datapoints

import "fmt"

type DataPointId struct {
	IntId int
	StrId string
}

type DataPoint struct {
	Value float64
	Id    DataPointId
}

type DataPointCollection struct {
	DataPoints []DataPoint
}

func (dp DataPoint) String() string {
	return fmt.Sprintf("%f", dp.Value)
}

func (dp *DataPoint) UpdateValue(v float64) {
	dp.Value = v
}

func (dp *DataPoint) Emit(c chan DataPointCollection) {
	c <- DataPointCollection{DataPoints: []DataPoint{*dp}}
}
