package util

import (
	"fmt"
	"log"
	"os/exec"
	"somedude/model"
)

type Solve = model.Solve

func CheckSolve(solve *Solve)string{
    path := getFiles(solve)
    copyTesterFile(path, solve)
    output := buildAndRun(path,solve)
    return output
}

func getFiles(solve *Solve) string{
    path := "solution/"+solve.User+"/"+solve.Title+"/"
    cmd,e := exec.Command("mkdir","-p",path).Output()
    log.Println(cmd)
    CheckError(e)
    cmd,e = exec.Command("curl", solve.File,"-o", path+"/"+solve.Title+".py").Output()
    CheckError(e)
    return path
}

func copyTesterFile(path string, solve *Solve){
    cmd, e := exec.Command("cp", "dockerfiles/"+solve.Title+"/"+"python/Dockerfile", path).Output()
    log.Println(cmd)
    CheckError(e)
    cmd, e = exec.Command("cp", "dockerfiles/"+solve.Title+"/"+"python/"+solve.Title+"Test.py", path).Output()
    log.Println(cmd)
    CheckError(e)
}

func buildAndRun(path string, solve *Solve) string{
    cmd := exec.Command("python3", path+"/"+solve.Title+"Test.py")
    out, err := cmd.CombinedOutput()
    CheckError(err)
    return string(out)
}

func CheckError(e error) {
    if e != nil {
        fmt.Println(e)
    }
}
