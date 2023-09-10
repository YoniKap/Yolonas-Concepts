### install dependencies on your environment :
pip install super-gradients==3.1.2

### Run The code
*make sure you are running the code froom the example directory*
- `Run example-picture.py to run YOLONAS on a picture `
- `Run example-video.py to run YOLONAS on a picture `
  - result will be stored in a file called "detected.mp4"


` in case of this error on your video run:`
```
 torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.17 GiB (GPU 0; 3.81 GiB total capacity; 1.95 GiB already allocated; 672.19 MiB free; 2.24 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
```
`no worries it just means your GPU memory is allocated to other proccses`<br>
`For a quick fix just edit the following line in example-video.py:`
```python
yolo_nas_l.to(device).predict(input_video_path).save(output_video_path)
```
`to this:`
```python
yolo_nas_l.to("cpu").predict(input_video_path).save(output_video_path)
```
this will run the code on your CPU rather then your GPU