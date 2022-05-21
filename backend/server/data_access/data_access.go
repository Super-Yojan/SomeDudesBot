package data_access;

import(
    "database/sql"
    _ "github.com/lib/pq"
    "fmt"
    "log"
)

var db *sql.DB

type Challenge struct{
    ID          int64   `JSON:"id"`
    Author      string  `JSON:"author"`
    Title       string  `JSON:"title"`
    Description string  `JSON:"desc"`
}


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

    _, err = db.Query("create table challenges (id INT PRIMARY KEY NOT NULL, author CHAR(50), title CHAR(50), description TEXT)")
    if err != nil {
        log.Fatalf("Error Creating Table challenges %d", err)
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


