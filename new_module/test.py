from openerp.osv import fields, osv
from openerp.tools.translate import _

class test(osv.osv):
    _name = "python.test"
    _columns = {
        'name' : fields.char('Name',size=1024,required=True),
        'code': fields.text('Code',required=True),
        'result':fields.text('Result',readonly=True),
        }
    
    def test(self,cr,uid,ids,context=None):
        localdict = {'self':self,'cr':cr,'uid':uid, 'context':context,'user_obj':self.pool.get('res.users').browse(cr,uid,uid,context=context)}
        for obj in self.browse(cr,uid,ids,context=context):
            try :
                exec obj.code in localdict
                if localdict.get('result', False):
                    self.write(cr,uid,ids,{'result':localdict['result']})
                else : 
                    self.write(cr,uid,ids,{'result':''})
            except Exception, e:
                raise osv.except_osv(_('Error !'), _('code is not able to run ! message : %s' %(e)))
        return True
