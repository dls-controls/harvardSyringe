from iocbuilder import AutoSubstitution
from iocbuilder.modules.streamDevice import AutoProtocol

class harvardSyringe(AutoSubstitution, AutoProtocol):
    # Substitution attributes
    TemplateFile = 'harvardSyringe.template'

    # AutoProtocol attributes
    ProtocolFiles = ['harvardSyringe.proto']


