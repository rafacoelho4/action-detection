# Action Detection

![GitHub repo size](https://img.shields.io/github/repo-size/rafacoelho4/action-detection?style=for-the-badge)

![Alt text](medio/img.jpg?raw=true "Title")

> Action detection with opencv project and object classification using yolo

## 💻 The project

There are three directories in this project:

simples: runs with the webcam and detects movement through comparison
from the first frame with all the following ones.

medio: processes external mp4 video (or webcam video) and detects motion
through constant comparison between the current frame and the previous one.

yolo: using the YOLO (You Only Look Once) library that works with an already trained network and
sorts 80 different objects.

Before starting, make sure you meet the following requirements:

- You have at least version 3.0 of `python`
- There's a webcam you can use (or mp4 videos to replace).
- You have downloaded `yolo`.

## 🚀 Installation

To install and run Action Detection, follow these simple steps:

```
git clone https://github.com/rafacoelho4/action-detection.git
```

Para usar <nome_do_projeto>, siga estas etapas:

### simple

Execute the python file camera.py

### medio

Run "motiondetection_webcam.py"

### yolo

```
cd yolo
```

Inside the directory you can run "yolo_webcam.py" or "yolo_mp4.py"

## 🤝 Contributors

This project exists thanks to all the people who contribute.

<table>
  <tr>
    <td align="center">
      <a href="#">
        <sub>
          <b>Rafael Coelho</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <sub>
          <b>Maria Laura Raimundo</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <sub>
          <b>Ananda Mendes</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## 📝 License

This project is under license. Open file [LICENSE](LICENSE.md) for more details.
