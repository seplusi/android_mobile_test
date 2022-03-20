How to execute this project:

Install python packages:
* pytest==7.1.0
* pytest-forked==1.4.0
* pytest-html==3.1.1
* pytest-metadata==1.11.0
* pytest-runner==4.2
* pytest-xdist==2.5.0

Download the github repo

Create 2 emulators:
* emulator-5554 : Android 10: Nexus S
* emulator-5556 : Android 11: Pixel 3a

Launch 2 appium servers with these specific ports:
* appium -p 4723
* appium -p 4724

To execute the tests just execute:
cd main/tests
pytest app1 --html=report.html

You'll see the following info

(venv3.7) tests % pytest app1 --html=report.html
================================================================== test session starts ==================================================================
platform darwin -- Python 3.7.12, pytest-7.1.0, pluggy-0.13.1
rootdir: /Users/luisarcanjo/PycharmProjects/pythonProject/main/tests, configfile: pytest.ini
plugins: xdist-2.5.0, forked-1.4.0, html-3.1.1, metadata-1.11.0
gw0 [4] / gw1 [4]
....                                                                                                                                              [100%]
-------------------------- generated html file: file:///Users/luisarcanjo/PycharmProjects/pythonProject/main/tests/report.html --------------------------
============================================================= 4 passed in 70.24s (0:01:10) ==============================================================
(venv3.7) tests %
