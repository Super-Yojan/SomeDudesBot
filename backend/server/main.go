package main

import (
    "somedude/helpers"
	_ "github.com/lib/pq"
	"github.com/gofiber/fiber/v2"
    "somedude/data_access"
)



// The starting place for the app..
func main(){
    data_access.Migrate() 
    app := fiber.New()
    helpers.SetupRoutes(app)
    app.Listen(":8080")
}
