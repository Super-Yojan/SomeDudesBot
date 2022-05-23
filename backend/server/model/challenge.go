package model

type Challenge struct{
    ID          int64   
    Author      string  
    Title       string 
    Description string
}

type Solve struct{
    ID          int64   `json:"ID"`
    User        string  `json:"User"`
    Title       string  `json:"Title"`
    File        string  `json:"File"`
}
