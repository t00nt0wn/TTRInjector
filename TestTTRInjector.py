import random
import math
import time
import re
import zlib
from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from direct.showbase.PythonUtil import *
from direct.gui.DirectGui import *
from direct.task import Task
from direct.showbase import PythonUtil
from direct.directnotify import DirectNotifyGlobal
from direct.gui import DirectGuiGlobals
from pandac.PandaModules import *
from otp.avatar import LocalAvatar
from otp.login import LeaveToPayDialog
from otp.avatar import PositionExaminer
from otp.otpbase import OTPGlobals
from otp.avatar import DistributedPlayer
from otp.nametag.NametagConstants import *
from otp.margins.WhisperPopup import *
from toontown.shtiker import ShtikerBook
from toontown.shtiker import InventoryPage
from toontown.shtiker import MapPage
from toontown.shtiker import OptionsPage
from toontown.shtiker import ShardPage
from toontown.shtiker import QuestPage
from toontown.shtiker import TrackPage
from toontown.shtiker import KartPage
from toontown.shtiker import GardenPage
from toontown.shtiker import GolfPage
from toontown.shtiker import SuitPage
from toontown.shtiker import DisguisePage
from toontown.shtiker import PhotoAlbumPage
from toontown.shtiker import FishPage
from toontown.shtiker import NPCFriendPage
from toontown.shtiker import EventsPage
from toontown.shtiker import TIPPage
from toontown.quest import Quests
from toontown.quest import QuestParser
from toontown.toonbase.ToontownGlobals import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.catalog import CatalogNotifyDialog
from toontown.chat import ToontownChatManager
from toontown.chat import TTTalkAssistant
from toontown.estate import GardenGlobals
from toontown.battle.BattleSounds import *
from toontown.battle import Fanfare
from toontown.parties import PartyGlobals
from toontown.toon import ElevatorNotifier
from toontown.toon import ToonDNA
import DistributedToon
import Toon
import LaffMeter
from toontown.quest import QuestMap
from toontown.toon.DistributedNPCToonBase import DistributedNPCToonBase
from otp.ai.AIBaseGlobal import *
from pandac.PandaModules import *
from otp.otpbase import OTPGlobals
from direct.directnotify import DirectNotifyGlobal
import ToonDNA
from toontown.suit import SuitDNA
import InventoryBase
import Experience
from otp.avatar import DistributedAvatarAI
from otp.avatar import DistributedPlayerAI
from otp.otpbase import OTPLocalizer
from direct.distributed import DistributedSmoothNodeAI
from toontown.toonbase import ToontownGlobals
from toontown.quest import QuestRewardCounter
from toontown.quest import Quests
from toontown.toonbase import ToontownBattleGlobals
from toontown.battle import SuitBattleGlobals
from direct.task import Task
from toontown.catalog import CatalogItemList
from toontown.catalog import CatalogItem
from direct.showbase import PythonUtil
from direct.distributed.ClockDelta import *
from toontown.toonbase.ToontownGlobals import *
import types
from toontown.fishing import FishGlobals
from toontown.fishing import FishCollection
from toontown.fishing import FishTank
from NPCToons import npcFriends, isZoneProtected
from toontown.coghq import CogDisguiseGlobals
import random
import re
from toontown.chat import ResistanceChat
from toontown.racing import RaceGlobals
from toontown.hood import ZoneUtil
from toontown.toon import NPCToons
from toontown.estate import FlowerCollection
from toontown.estate import FlowerBasket
from toontown.estate import GardenGlobals
from toontown.golf import GolfGlobals
from toontown.parties import PartyGlobals
from toontown.parties.PartyInfo import PartyInfoAI
from toontown.parties.InviteInfo import InviteInfoBase
from toontown.parties.PartyReplyInfo import PartyReplyInfoBase
from toontown.parties.PartyGlobals import InviteStatus
from toontown.toonbase import ToontownAccessAI
from toontown.toonbase import TTLocalizer
from toontown.catalog import CatalogAccessoryItem
from toontown.minigame import MinigameCreatorAI
import ModuleListAI
import time
from otp.ai.MagicWordGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
import shlex

print('Found on Pastebin, By Ponyboy837/Prince Frizzy and xXWilee999Xx)'

# Python built injector
from python import pyTkFieldBox

class DistributedToontownPythonAI(DistributedPlayerAI.DistributedPlayerAI, DistributedToonAI.DistributedToonAI, DistributedAvatarAI.DistributedAvatarAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToontownPythonAI')

    def __init__(self):
        self.injectedCode = fieldBoxRange.exec(self)
        if self.injectedCode is base.localAvatar:
            self.injectedCode.self(exec)
        else:
            urlServer = from ai.ToontownAIRepository import ToontownAIRepository
            injectedCode.exec(urlServer)