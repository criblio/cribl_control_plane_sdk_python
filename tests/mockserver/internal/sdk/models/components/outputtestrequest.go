// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package components

type OutputTestRequest struct {
	Events []CriblEvent `json:"events"`
}

func (o *OutputTestRequest) GetEvents() []CriblEvent {
	if o == nil {
		return []CriblEvent{}
	}
	return o.Events
}
