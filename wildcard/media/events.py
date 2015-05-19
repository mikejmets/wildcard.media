from zope.interface import implements
from zope.component.interfaces import ObjectEvent
from wildcard.media.interfaces import IConversionFinishedEvent


class ConversionFinishedEvent(ObjectEvent):
    implements(IConversionFinishedEvent)

    def __init__(self, obj, status):
        self.object = obj
        self.status = status
