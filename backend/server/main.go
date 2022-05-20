package main

import (
    "net/http"
    "strings"
    "github.com/gin-gonic/gin"
)

type solve struct {
    ID      int     `json:"id"`
    User    string  `json:"user"`
    File    string  `json:"file"`
}

func sayHello(w http.ResponseWriter, r *http.Request){
    message := r.URL.Path
    message = strings.TrimPrefix(message, "/")
    message = "Hello "+message
    w.Write([]byte(message))
}




func getSolve(solve *gin.Context){



}


func main(){
    http.HandleFunc("/",sayHello)

    if err := http.ListenAndServe(":8080", nil); err != nil{
        panic(err)
    }
}
