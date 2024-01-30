# from flask import Flask, send_file
# import matlab.engine

# app = Flask(__name__)
# eng = matlab.engine.start_matlab()

# @app.route('/process_image')
# def process_image():
#     # Run your MATLAB script
#     eng.Porp(nargout=0)
#     # Send the processed image
#     return send_file('porp/porphyrin.jpg', mimetype='image/jpeg')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, send_file
from flask_cors import CORS
import matlab.engine

app = Flask(__name__)
CORS(app)
eng = matlab.engine.start_matlab()

@app.route('/process_image')
def process_image():
    try:
        print("Processing started.")
        # Run your MATLAB script
        eng.Porp(nargout=0)
        print("Processing completed.")
        # Send the processed image
        return send_file('porp/porphyrin.jpg', mimetype='image/png')
    except Exception as e:
        print(f"Error: {e}")
        return "Error in processing image", 500


if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, Response
# import matlab.engine
# import io
# from PIL import Image
# import numpy as np

# app = Flask(__name__)
# eng = matlab.engine.start_matlab()

# @app.route('/process_image')
# def process_image():
#     # Run your MATLAB script
#     img_matrix = eng.process_image_from_web(nargout=1)
    
#     # Convert MATLAB matrix to numpy array
#     np_img = np.array(img_matrix, dtype=np.uint8)
    
#     # Convert numpy array to a PIL Image
#     img = Image.fromarray(np_img)
    
#     # Save PIL Image to bytes
#     img_byte_array = io.BytesIO()
#     img.save(img_byte_array, format="JPEG")
    
#     return Response(img_byte_array.getvalue(), mimetype='image/jpeg')

# if __name__ == '__main__':
#     app.run(debug=True)

