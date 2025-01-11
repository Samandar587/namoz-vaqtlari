package app

import (
	"fmt"
	"os"

	"golang-project-template/cmd/app/servers"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{Use: "run-grpc"}

// command to run http server
var httpCmd = &cobra.Command{
	Use: "http-server",
	Run: func(cmd *cobra.Command, args []string) {
		servers.RunHttpServer()
	},
}

func Execute() {
	rootCmd.AddCommand(httpCmd)

	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintf(os.Stderr, "error while executing your CLI '%s'", err)
		os.Exit(1)
	}
}
