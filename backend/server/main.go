package main

import (
	"github.com/gofiber/fiber/v2"
	_ "github.com/lib/pq"
	"somedude/data_access"
	"somedude/helpers"
)

// The starting place for the app..
func main() {
	data_access.Migrate()
	app := fiber.New()
	helpers.SetupRoutes(app)
	app.Listen(":8080")
}
