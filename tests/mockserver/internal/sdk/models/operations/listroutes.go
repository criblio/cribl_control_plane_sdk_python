// Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT.

package operations

import (
	"mockserver/internal/sdk/models/components"
)

// ListRoutesResponseBody - a list of Routes objects
type ListRoutesResponseBody struct {
	// number of items present in the items array
	Count *int64              `json:"count,omitempty"`
	Items []components.Routes `json:"items,omitempty"`
}

func (o *ListRoutesResponseBody) GetCount() *int64 {
	if o == nil {
		return nil
	}
	return o.Count
}

func (o *ListRoutesResponseBody) GetItems() []components.Routes {
	if o == nil {
		return nil
	}
	return o.Items
}

type ListRoutesResponse struct {
	HTTPMeta components.HTTPMetadata `json:"-"`
	// a list of Routes objects
	Object *ListRoutesResponseBody
}

func (o *ListRoutesResponse) GetHTTPMeta() components.HTTPMetadata {
	if o == nil {
		return components.HTTPMetadata{}
	}
	return o.HTTPMeta
}

func (o *ListRoutesResponse) GetObject() *ListRoutesResponseBody {
	if o == nil {
		return nil
	}
	return o.Object
}
