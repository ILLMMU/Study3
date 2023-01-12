#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on May 04, 2021, at 14:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'PRACTICE_OneBack_Digits'  # from the Builder filename that created this script
expInfo = {'Gender (f/m)': '', 'Age': '', 'participant': '', 'Ethnic': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\lighting\\Desktop\\Siraji\\Auditory 1-Back PsychoPy\\PRACTICE_OneBack_Digits_Auditory_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Background_1 = visual.EnvelopeGrating(
    win=win, name='Background_1',units='norm', 
    carrier=None, mask=None,
    ori=0, pos=(0, 0), size=(20),
    sf=1.0, phase=0.0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb',
     opacity=1, contrast=0.5,
    texRes=128, envelope='sin',
    envori=0.0, envsf=1.0,
    envphase=0.0, power=1.0,
    moddepth=1.0, blendmode='avg', beat=False, interpolate=True, depth=0.0)
if sys.version[0]=='3' and np.min(win.gamma) == None:
    logging.warning('Envelope grating in use with no gamma set. Unless you have hardware gamma correction the image will be distorted.')
elif np.min(win.gamma) < 1.01:
    logging.warning('Envelope grating in use with window gamma <= 1.0 or no gamma set at all. Unless you have hardware gamma correction the image will be distorted.')
text_2 = visual.TextStim(win=win, name='text_2',
    text='Welcome to the Auditory One Back Task (PRACTICE)!',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "Inst"
InstClock = core.Clock()
Background_2 = visual.EnvelopeGrating(
    win=win, name='Background_2',units='norm', 
    carrier=None, mask=None,
    ori=0, pos=(0, 0), size=(20),
    sf=1.0, phase=0.0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb',
     opacity=1, contrast=0.5,
    texRes=128, envelope='sin',
    envori=0.0, envsf=1.0,
    envphase=0.0, power=1.0,
    moddepth=1.0, blendmode='avg', beat=False, interpolate=True, depth=0.0)
if sys.version[0]=='3' and np.min(win.gamma) == None:
    logging.warning('Envelope grating in use with no gamma set. Unless you have hardware gamma correction the image will be distorted.')
elif np.min(win.gamma) < 1.01:
    logging.warning('Envelope grating in use with window gamma <= 1.0 or no gamma set at all. Unless you have hardware gamma correction the image will be distorted.')
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

PartiNum = expInfo['participant']
PartiNum = int(PartiNum)

KeyList = ['N','V']

check = PartiNum%2

if check == 0:
    Key = KeyList[0]
    # Even Target = N
    InstKey = 'You will hear numbers read aloud, one number at a time.\n\nWhen the number heard matches the last number presented, press the N key.\n\nWhen the number heard does NOT match the last number presented, press the V key.\n\nPlease try to respond as accurately and as fast as possible.\n\nYou can start responding at the SECOND number you hear onwards. \n\nPress SPACEBAR to begin.'
else:
    Key = KeyList[1]
    # Odd Target = v
    InstKey = 'You will hear numbers read aloud, one number at a time.\n\nWhen the number heard matches the last number presented, press the V key.\n\nWhen the number heard does NOT match the last number presented, press the N key.\n\nPlease try to respond as accurately and as fast as possible.\n\nYou can start responding at the SECOND number you hear onwards. \n\nPress SPACEBAR to begin.'





# Initialize components for Routine "Block1"
Block1Clock = core.Clock()
Background_3 = visual.EnvelopeGrating(
    win=win, name='Background_3',units='norm', 
    carrier=None, mask=None,
    ori=0, pos=(0, 0), size=(20),
    sf=1.0, phase=0.0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb',
     opacity=1, contrast=0.5,
    texRes=128, envelope='sin',
    envori=0.0, envsf=1.0,
    envphase=0.0, power=1.0,
    moddepth=1.0, blendmode='avg', beat=False, interpolate=True, depth=0.0)
if sys.version[0]=='3' and np.min(win.gamma) == None:
    logging.warning('Envelope grating in use with no gamma set. Unless you have hardware gamma correction the image will be distorted.')
elif np.min(win.gamma) < 1.01:
    logging.warning('Envelope grating in use with window gamma <= 1.0 or no gamma set at all. Unless you have hardware gamma correction the image will be distorted.')
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Stimulus = sound.Sound('A', secs=0.75, stereo=True, hamming=True,
    name='Stimulus')
Stimulus.setVolume(1)
StimResp = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
Background_4 = visual.EnvelopeGrating(
    win=win, name='Background_4',units='norm', 
    carrier=None, mask=None,
    ori=0, pos=(0, 0), size=(20),
    sf=1.0, phase=0.0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb',
     opacity=1, contrast=0.5,
    texRes=128, envelope='sin',
    envori=0.0, envsf=1.0,
    envphase=0.0, power=1.0,
    moddepth=1.0, blendmode='avg', beat=False, interpolate=True, depth=0.0)
if sys.version[0]=='3' and np.min(win.gamma) == None:
    logging.warning('Envelope grating in use with no gamma set. Unless you have hardware gamma correction the image will be distorted.')
elif np.min(win.gamma) < 1.01:
    logging.warning('Envelope grating in use with window gamma <= 1.0 or no gamma set at all. Unless you have hardware gamma correction the image will be distorted.')
text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "BreakMessage"
BreakMessageClock = core.Clock()
Background_5 = visual.EnvelopeGrating(
    win=win, name='Background_5',units='norm', 
    carrier=None, mask=None,
    ori=0, pos=(0, 0), size=(20),
    sf=1.0, phase=0.0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb',
     opacity=1, contrast=0.5,
    texRes=128, envelope='sin',
    envori=0.0, envsf=1.0,
    envphase=0.0, power=1.0,
    moddepth=1.0, blendmode='avg', beat=False, interpolate=True, depth=0.0)
if sys.version[0]=='3' and np.min(win.gamma) == None:
    logging.warning('Envelope grating in use with no gamma set. Unless you have hardware gamma correction the image will be distorted.')
elif np.min(win.gamma) < 1.01:
    logging.warning('Envelope grating in use with window gamma <= 1.0 or no gamma set at all. Unless you have hardware gamma correction the image will be distorted.')
BreakMsg = visual.TextStim(win=win, name='BreakMsg',
    text='Take a break!',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
BreakResp = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
Background_6 = visual.EnvelopeGrating(
    win=win, name='Background_6',units='norm', 
    carrier=None, mask=None,
    ori=0, pos=(0, 0), size=(20),
    sf=1.0, phase=0.0,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb',
     opacity=1, contrast=0.5,
    texRes=128, envelope='sin',
    envori=0.0, envsf=1.0,
    envphase=0.0, power=1.0,
    moddepth=1.0, blendmode='avg', beat=False, interpolate=True, depth=0.0)
if sys.version[0]=='3' and np.min(win.gamma) == None:
    logging.warning('Envelope grating in use with no gamma set. Unless you have hardware gamma correction the image will be distorted.')
elif np.min(win.gamma) < 1.01:
    logging.warning('Envelope grating in use with window gamma <= 1.0 or no gamma set at all. Unless you have hardware gamma correction the image will be distorted.')
text_4 = visual.TextStim(win=win, name='text_4',
    text='End of the Auditory One Back Task (PRACTICE)!\n\n\nThank you for your participation!',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
# keep track of which components have finished
WelcomeComponents = [Background_1, text_2, key_resp_3]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Background_1* updates
    if Background_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Background_1.frameNStart = frameN  # exact frame index
        Background_1.tStart = t  # local t and not account for scr refresh
        Background_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Background_1, 'tStartRefresh')  # time at next scr refresh
        Background_1.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Inst"-------
# update component parameters for each repeat
text.setText(InstKey)
key_resp_2.keys = []
key_resp_2.rt = []
# keep track of which components have finished
InstComponents = [Background_2, text, key_resp_2]
for thisComponent in InstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Inst"-------
while continueRoutine:
    # get current time
    t = InstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Background_2* updates
    if Background_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Background_2.frameNStart = frameN  # exact frame index
        Background_2.tStart = t  # local t and not account for scr refresh
        Background_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Background_2, 'tStartRefresh')  # time at next scr refresh
        Background_2.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Inst"-------
for thisComponent in InstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('OneBackCond-practice.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block1"-------
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    Stimulus.setSound(Stim, secs=0.75, hamming=True)
    Stimulus.setVolume(1, log=False)
    StimResp.keys = []
    StimResp.rt = []
    #nCorr = trials.data['StimResp.corr'].sum() #.std(), .mean() also available
    #meanRt = trials.data['StimResp.rt'].mean()
    #msg = "You got %i trials correct (rt=%.2f)" %(nCorr,meanRt)
    # keep track of which components have finished
    Block1Components = [Background_3, Fixation, Stimulus, StimResp]
    for thisComponent in Block1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Block1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Background_3* updates
        if Background_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Background_3.frameNStart = frameN  # exact frame index
            Background_3.tStart = t  # local t and not account for scr refresh
            Background_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Background_3, 'tStartRefresh')  # time at next scr refresh
            Background_3.setAutoDraw(True)
        if Background_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Background_3.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                Background_3.tStop = t  # not accounting for scr refresh
                Background_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Background_3, 'tStopRefresh')  # time at next scr refresh
                Background_3.setAutoDraw(False)
        
        # *Fixation* updates
        if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.tStart = t  # local t and not account for scr refresh
            Fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
            Fixation.setAutoDraw(True)
        if Fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Fixation.tStop = t  # not accounting for scr refresh
                Fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                Fixation.setAutoDraw(False)
        # start/stop Stimulus
        if Stimulus.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Stimulus.frameNStart = frameN  # exact frame index
            Stimulus.tStart = t  # local t and not account for scr refresh
            Stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            Stimulus.play(when=win)  # sync with win flip
        if Stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimulus.tStartRefresh + 0.75-frameTolerance:
                # keep track of stop time/frame for later
                Stimulus.tStop = t  # not accounting for scr refresh
                Stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimulus, 'tStopRefresh')  # time at next scr refresh
                Stimulus.stop()
        
        # *StimResp* updates
        waitOnFlip = False
        if StimResp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            StimResp.frameNStart = frameN  # exact frame index
            StimResp.tStart = t  # local t and not account for scr refresh
            StimResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StimResp, 'tStartRefresh')  # time at next scr refresh
            StimResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(StimResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(StimResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if StimResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StimResp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                StimResp.tStop = t  # not accounting for scr refresh
                StimResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(StimResp, 'tStopRefresh')  # time at next scr refresh
                StimResp.status = FINISHED
        if StimResp.status == STARTED and not waitOnFlip:
            theseKeys = StimResp.getKeys(keyList=['v', 'n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                StimResp.keys = theseKeys.name  # just the last key pressed
                StimResp.rt = theseKeys.rt
                # was this 'correct'?
                if (StimResp.keys == str(CorrAns)) or (StimResp.keys == CorrAns):
                    StimResp.corr = 1
                else:
                    StimResp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block1"-------
    for thisComponent in Block1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Fixation.started', Fixation.tStartRefresh)
    trials.addData('Fixation.stopped', Fixation.tStopRefresh)
    Stimulus.stop()  # ensure sound has stopped at end of routine
    trials.addData('Stimulus.started', Stimulus.tStartRefresh)
    trials.addData('Stimulus.stopped', Stimulus.tStopRefresh)
    # check responses
    if StimResp.keys in ['', [], None]:  # No response was made
        StimResp.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           StimResp.corr = 1;  # correct non-response
        else:
           StimResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('StimResp.keys',StimResp.keys)
    trials.addData('StimResp.corr', StimResp.corr)
    if StimResp.keys != None:  # we had a response
        trials.addData('StimResp.rt', StimResp.rt)
    trials.addData('StimResp.started', StimResp.tStartRefresh)
    trials.addData('StimResp.stopped', StimResp.tStopRefresh)
    NoRESP = 0
    nCorr_fault = 0
    NoRESP_fault = 0
    StimRespCorr = trials.data['StimResp.corr']
    StimRespRT = trials.data['StimResp.keys']
    
    for i in StimRespRT:
        if not i:
            NoRESP = NoRESP + 1
    
    #test for Non-numeric values & convert them to 0 for first trial
    temp_NoResp = StimRespRT[0]
    
    if temp_NoResp == None:
        temp_NoResp = 0
    else:
        temp_NoResp = temp_NoResp
    #for k in temp_NoResp:
    #    if not k:
    #        NoRESP_fault = 0
    #    else:
    #        NoRESP_fault = 1
    if temp_NoResp > 0:
        NoRESP_fault = 0
    else:
        NoRESP_fault = 1
    
    nMissed = NoRESP - NoRESP_fault
    
    nCorr = trials.data['StimResp.corr'].sum() #.std(), .mean() also available
    
    temp_nCorr = StimRespCorr[0]
    #for j in temp_nCorr:
    #   if j == 1:
    #        nCorr_fault = 1
    if temp_nCorr == 1:
        nCorr_fault = 1
    else:
        nCorr_fault = 0
    
    nCorr = nCorr - nCorr_fault
    
    nWrong = 22-nMissed-nCorr
    
    HitRate = (nCorr)/22*100
    
    #msg = " Correct Trials = %i trials \n Wrong Trials = %i \n Hit rate = %.2f" %(nCorr, nWrong, HitRate)
    
    PartiNum = expInfo['participant']
    PartiNum = int(PartiNum)
    
    check = PartiNum%2
    
    if check == 0:
        nCorr = nWrong
        nWrong = 22-nMissed-nCorr
        HitRate = (nCorr)/22*100
    
    msg = " Correct Trials = %i trials \n Wrong Trials = %i \n Missed trials = %i \n Hit rate = %.2f" %(nCorr, nWrong, nMissed, HitRate)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Feedback"-------
# update component parameters for each repeat
text_3.setText(msg )
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
FeedbackComponents = [Background_4, text_3, key_resp_4]
for thisComponent in FeedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Feedback"-------
while continueRoutine:
    # get current time
    t = FeedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Background_4* updates
    if Background_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Background_4.frameNStart = frameN  # exact frame index
        Background_4.tStart = t  # local t and not account for scr refresh
        Background_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Background_4, 'tStartRefresh')  # time at next scr refresh
        Background_4.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Feedback"-------
for thisComponent in FeedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BreakMessage"-------
# update component parameters for each repeat
BreakResp.keys = []
BreakResp.rt = []
# keep track of which components have finished
BreakMessageComponents = [Background_5, BreakMsg, BreakResp]
for thisComponent in BreakMessageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BreakMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "BreakMessage"-------
while continueRoutine:
    # get current time
    t = BreakMessageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BreakMessageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Background_5* updates
    if Background_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Background_5.frameNStart = frameN  # exact frame index
        Background_5.tStart = t  # local t and not account for scr refresh
        Background_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Background_5, 'tStartRefresh')  # time at next scr refresh
        Background_5.setAutoDraw(True)
    
    # *BreakMsg* updates
    if BreakMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BreakMsg.frameNStart = frameN  # exact frame index
        BreakMsg.tStart = t  # local t and not account for scr refresh
        BreakMsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BreakMsg, 'tStartRefresh')  # time at next scr refresh
        BreakMsg.setAutoDraw(True)
    
    # *BreakResp* updates
    waitOnFlip = False
    if BreakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BreakResp.frameNStart = frameN  # exact frame index
        BreakResp.tStart = t  # local t and not account for scr refresh
        BreakResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BreakResp, 'tStartRefresh')  # time at next scr refresh
        BreakResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BreakResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BreakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BreakResp.status == STARTED and not waitOnFlip:
        theseKeys = BreakResp.getKeys(keyList=None, waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            BreakResp.keys = theseKeys.name  # just the last key pressed
            BreakResp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BreakMessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BreakMessage"-------
for thisComponent in BreakMessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if BreakResp.keys in ['', [], None]:  # No response was made
    BreakResp.keys = None
thisExp.addData('BreakResp.keys',BreakResp.keys)
if BreakResp.keys != None:  # we had a response
    thisExp.addData('BreakResp.rt', BreakResp.rt)
thisExp.nextEntry()
# the Routine "BreakMessage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End"-------
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
# keep track of which components have finished
EndComponents = [Background_6, text_4, key_resp_5]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Background_6* updates
    if Background_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Background_6.frameNStart = frameN  # exact frame index
        Background_6.tStart = t  # local t and not account for scr refresh
        Background_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Background_6, 'tStartRefresh')  # time at next scr refresh
        Background_6.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
print(PartiNum)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
