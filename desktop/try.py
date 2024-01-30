import matlab.engine

# Start MATLAB engine
eng = matlab.engine.start_matlab()

eng.addpath('./', nargout=0)

eng.Porp(nargout=0)

# Stop the MATLAB engine
eng.quit()
