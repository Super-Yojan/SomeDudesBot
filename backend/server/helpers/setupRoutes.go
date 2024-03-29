package helpers;

import (
    "somedude/controllers"
    "github.com/gofiber/fiber/v2"
)

func SetupRoutes(app *fiber.App){
    app.Get("/", controllers.ChallengesGet)
    app.Post("/", controllers.ChallengesPost)
    app.Post("/solve", controllers.ChallengeSolve)
}
