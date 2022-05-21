package data_access;

import(
    "database/sql"
    _ "github.com/lib/pq"
    "fmt"
    "log"
    "somedude/model"
)

var db *sql.DB

type Challenge = model.Challenge


func Migrate(){
    connStr := "postgresql://postgres:somedudesbot@db/somedudes?sslmode=disable"
    var err error
    db,err = sql.Open("postgres", connStr)
	if err != nil {
		log.Fatalf("Problem migrating database %v", err)
	}

    pingErr := db.Ping()

    if pingErr != nil{
        log.Fatalf("Cannot Ping the database %d", err)
    }

    fmt.Printf("Database Connected")

    _, err = db.Query("create table challenges (id SERIAL PRIMARY KEY NOT NULL, author CHAR(50), title CHAR(50), description TEXT)")
    if err != nil {
        log.Printf("Error Creating Table challenges %d", err)
    }

}

func GetChallenges() ([]Challenge, error){
    var challenges []Challenge
    rows, err := db.Query("SELECT * FROM challenges")
    if err != nil {
        log.Fatal(err)
    }
    for rows.Next() {
        var challenge Challenge
        if err:= rows.Scan(&challenge.ID, &challenge.Author, &challenge.Title, &challenge.Description); err != nil {
            return nil, fmt.Errorf("%v", err);
        }
        challenges = append(challenges, challenge)
    }
    return challenges, nil
}

func AddChallenge(chal *Challenge) error{
    fmt.Printf("%v, %v, %v", chal.Author, chal.Title, chal.Description)
    _, err := db.Exec("INSERT INTO challenges ( author, title, description) VALUES ($1, $2, $3)", chal.Author, chal.Title, chal.Description)
    return err
}

