#coding=utf-8
from .manager import CephManager
from api.error import Error
from api.error import ERR_CEPHPOOL_ID


class CephStorageAPI(object):
    def __init__(self, manager=None):
        if manager:
            self.manager = manager
        else:
            self.manager = CephManager()
        super().__init__()
    
    def get_pool_list_by_center_id(self, center_id):
        return self.manager.get_pool_list_by_center_id(center_id)

    def get_pool_by_id(self, cephpool_id):
        return self.manager.get_pool_by_id(cephpool_id)

    def get_volume_pool_by_center_id(self, center_id):
        return self.manager.get_volume_pool_by_center_id(center_id)

    def clone(self, cephpool_id, src, dst):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.clone(src, dst)

    def mv(self, cephpool_id, src, dst):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.mv(src, dst)

    def rm(self, cephpool_id, dst):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.rm(dst)

    def exists(self, cephpool_id, name):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.exists(name)

    def create_snap(self, cephpool_id, name):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.create_snap(name)

    def protect_snap(self, cephpool_id, name):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.protect_snap(name)

    def create(self, cephpool_id, name, size):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.create(name, size)

    def resize(self, cephpool_id, name, size):
        cephpool = self.get_pool_by_id(cephpool_id)
        return cephpool.resize(name, size)
        