# include <stdio.h>		// Required for printf()
# include <stdlib.h>	// Required for atoi() (if converting to int)

int main( int argc, char *argv[]){
	// Print the total number of arguments
	printf("Number if arguments (argc): %d\n", argc);
	
	// Loop through and print each argument 
	printf("arguments received:\n");
	for (int i = 0; i < argc; i++){
		printf("  argv[%d]: %s\n", i, argv[i]);
	}
	
	
	// Example of use an argument (e.g., expecting a number)
	
	if (argc > 1) { // Check if atleast one argument baside program name is provided
	printf("\nFirst argument (argv[1]): %s\n", argv[1]);
	
	// If we expect a number, conver the string to an integer 
	
	int num = atoi(argv[1]);   // atoi converts string to integer 
	printf("First argument as integer: %d\n", num );
	
	} else {
		printf("\nNo additional arguments provided. \n");
	}
	
	return 0;	// Indicate successful execution
	
}


