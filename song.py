class song:
        number=0
        verseNum=0
        verseTime=0
        chorusTime=0
        endTime=0
        chorus=0

        def __init__(self, Song_Number=0,Chorus=0, Verse_count=0, Verse_time=0,
                     Chorus_time=0, end_Time=0):
                self.number = Song_Number
                self.chorus = Chorus
                self.verseNum = Verse_count
                self.verseTime = Verse_time
                self.chorusTime = Chorus_time
                self.endTime = end_Time

        def __str__(self):
                return ("%-5d%-14d%-10d%-10d%-10d%d" % (self.chorus, self.number,
                                                        self.verseNum, self.verseTime,
                                                        self.chorusTime, self.endTime))
        
        def getNumber(self):
                return self.number

        def getverseNum(self):
                return self.verseNum

        def getverseTime(self):
                return self.verseTime

        def getchorusTime(self):
                return self.chorusTime

        def getendTime(self):
                return self.endTime

        def setNumber(self, num):
                self.number = num

        def setverseNum(self, num):
                self.verseNum = num

        def setverseTime(self, num):
                self.verseTime = num

        def setchorusTime(self, num):
                self.chorusTime = num

        def setendTime(self):
                self.endTime = num
        
