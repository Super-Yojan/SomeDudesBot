package controllers


import (
    "somedude/data_access"
    "github.com/gofiber/fiber/v2"
    "log"
)


type Challenge struct{
    ID          int64   `JSON:"id"`
    Author      string  `JSON:"author"`
    Title       string  `JSON:"title"`
    Description string  `JSON:"desc"`
}


func Helloworld(c *fiber.Ctx) error {
    return c.SendString("Hello");
}

//                         return type
func ChallengesGet(c *fiber.Ctx) error{
    challenge, err := data_access.GetChallenges()
    if err != nil {
        log.Output(0, "After getting ChallengesGet")
        log.Fatal(err);
    }
    return c.JSON(challenge)
}
