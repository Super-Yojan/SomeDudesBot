package controllers

import (
	"log"
	"somedude/data_access"
	"github.com/gofiber/fiber/v2"
    "somedude/model"
)

type Challenge = model.Challenge

type Respone struct{
    Success     bool
    Message     string
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

func ChallengesPost(c *fiber.Ctx) error{
    newChallenge := Challenge{}
    if err := c.BodyParser(&newChallenge); err != nil{
        log.Printf("Error parsing body %d", err);
    }
    err := data_access.AddChallenge(&newChallenge)
    if err != nil{
        return c.JSON(fiber.Map{
            "Success": false,
            "Message": "Failed to add challenge",
        })

    }
    rsp := Respone{
        Success: true,
        Message: "Adding Completed",
    }

    return c.JSON(rsp)
}

