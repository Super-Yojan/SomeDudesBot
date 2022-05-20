package main

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	_ "github.com/lib/pq"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/template/html"
)

// Struct format that defines id, username, and filename
type solve struct {
	ID   int    `json:"id"`
	User string `json:"user"`
	File string `json:"file"`
}

// Get  Handler to get challenge information
func getHandler(c *fiber.Ctx, db *sql.DB) error {
	var res string
	var program []string
	rows, err := db.Query("SELECT * FROM challenges")
	defer rows.Close()

	if err != nil {
		log.Fatalln(err)
		c.JSON("An error occured")
	}

	for rows.Next() {
		var r solve
		rows.Scan(&r.ID, &r.User, &r.File)
		program = append(program, res)
	}

	return c.Render("index", fiber.Map{
		"Todos": program,
	})
}

//Post handler to post solution
func postHandler(c *fiber.Ctx, db *sql.DB) error {
	return c.SendString("Hello")
}

// Main Function
func main() {

	// Database info
	connStr := "postgresql://postgres:somedudesbot@127.0.0.1/somedudes?sslmode=disable"

	// Connect to database
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}

	// Create a new app
	engine := html.New("./challenges", ".html")

	app := fiber.New(fiber.Config{
		Views: engine,
	})
	// app := fiber.New()

	//Gets challenges
	app.Get("/", func(c *fiber.Ctx) error {
		return getHandler(c, db)
	})

	// Posts challenge solution
	app.Post("/", func(c *fiber.Ctx) error {
		return postHandler(c, db)
	})

	// Start Server Here
	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}
	log.Fatalln(app.Listen(fmt.Sprintf(":%v", port)))
}
