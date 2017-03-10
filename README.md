# Hashcode_online_2017

This project is a solution of the **Google Hashcode 2017** online qualification round
  

The input folder is the folder where to put each _*.in_ files.  
The solutions are generated in the ouput folder with the same name as _*.in_ file but with _*.out_ extension.
  

You got 4 big functions: 
- `import_input` in input.py which reads from the input file and put in variables (stored in V class)
- `solve` in solution.py which is (at the moment) a very bad solver
- `export_output` in output.py which exports the results in .out files
- `rank` in ranking.py which returns the score of the given input

You can run:
- `./install.sh` to install everything needed in the project (only python3 here but you can add external libraries here)
- `./launch.sh` to execute the `main()` function and to compress _*.py_ files into a _ouputs/source_code.tar.gz_ to send the source code to the judge system
