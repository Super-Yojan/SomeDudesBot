package model

type Challenge struct {
	ID          int64  `json:"ID"`
	Author      string `json:"Author"`
	Title       string `json:"Title"`
	Description string `json:"Description"`
}

type Solve struct {
	ID    int64  `json:"ID"`
	User  string `json:"User"`
	Title string `json:"Title"`
	File  string `json:"File"`
}
