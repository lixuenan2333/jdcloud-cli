# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from argparse import RawTextHelpFormatter
from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class RdsController(BaseController):
    class Meta:
        label = 'rds'
        help = '使用该子命令操作rds相关资源'
        description = '''
        rds cli 子命令，可以使用该子命令操作rds相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/382/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--account-name'], dict(help="""(string) 用户名 """, dest='accountName', required=True)),
            (['--account-password'], dict(help="""(string) 用户密码 """, dest='accountPassword', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建数据库账户 ''',
        description='''
            创建数据库账户。

            示例: jdc rds create-account  --instance-id xxx --account-name xxx --account-password xxx
        ''',
    )
    def create_account(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.CreateAccountRequest import CreateAccountRequest
            params_dict = collect_user_args(self.app)
            req = CreateAccountRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--account-name'], dict(help="""(string) 账户名 """, dest='accountName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除数据库账户 ''',
        description='''
            删除数据库账户。

            示例: jdc rds delete-account  --instance-id xxx --account-name xxx
        ''',
    )
    def delete_account(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.DeleteAccountRequest import DeleteAccountRequest
            params_dict = collect_user_args(self.app)
            req = DeleteAccountRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--account-name'], dict(help="""(string) 账户名 """, dest='accountName', required=True)),
            (['--account-privileges'], dict(help="""(array: accountPrivilege) 账号的访问权限 """, dest='accountPrivileges', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 数据库账号授权 ''',
        description='''
            数据库账号授权。

            示例: jdc rds grant-privilege  --instance-id xxx --account-name xxx --account-privileges [{"":""}]
        ''',
    )
    def grant_privilege(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.GrantPrivilegeRequest import GrantPrivilegeRequest
            params_dict = collect_user_args(self.app)
            req = GrantPrivilegeRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--account-name'], dict(help="""(string) 账户名 """, dest='accountName', required=True)),
            (['--account-password'], dict(help="""(string) 新密码 """, dest='accountPassword', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 数据库账号重置密码 ''',
        description='''
            数据库账号重置密码。

            示例: jdc rds reset-password  --instance-id xxx --account-name xxx --account-password xxx
        ''',
    )
    def reset_password(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.ResetPasswordRequest import ResetPasswordRequest
            params_dict = collect_user_args(self.app)
            req = ResetPasswordRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--auto'], dict(help="""(int) 查询备份类型，0为手动备份，1为自动备份，不传表示全部. - 测试参数，后续可能被其他参数取代 """, dest='auto', required=False)),
            (['--backup-type-filter'], dict(help="""(string) 返回backupType等于指定值的备份列表。full为全量备份，diff为增量备份- 测试参数，后续可能被其他参数取代 """, dest='backupTypeFilter', required=False)),
            (['--db-name-filter'], dict(help="""(string) 返回dbName等于指定值的备份列表，不传或为空返回全部- 测试参数，后续可能被其他参数取代 """, dest='dbNameFilter', required=False)),
            (['--backup-time-range-start-filter'], dict(help="""(string) 返回备份开始时间大于该时间的备份列表- 测试参数，后续可能被其他参数取代 """, dest='backupTimeRangeStartFilter', required=False)),
            (['--backup-time-range-end-filter'], dict(help="""(string) 返回备份开始时间小于等于该时间的备份列表- 测试参数，后续可能被其他参数取代 """, dest='backupTimeRangeEndFilter', required=False)),
            (['--page-number'], dict(help="""(int) 显示数据的页码，取值范围：[1,1000)，页码超过总页数时，显示最后一页，用于查询列表的接口 """, dest='pageNumber', required=True)),
            (['--page-size'], dict(help="""(int) 每页显示的数据条数，取值范围：10/20/30/50/100 """, dest='pageSize', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取备份信息 ''',
        description='''
            获取备份信息。

            示例: jdc rds describe-backups  --instance-id xxx --page-number 0 --page-size 0
        ''',
    )
    def describe_backups(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.DescribeBackupsRequest import DescribeBackupsRequest
            params_dict = collect_user_args(self.app)
            req = DescribeBackupsRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 集群ID """, dest='instanceId', required=False)),
            (['--backup-spec'], dict(help="""(backupSpec) 备份规格 """, dest='backupSpec', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建备份 ''',
        description='''
            创建备份。

            示例: jdc rds create-backup 
        ''',
    )
    def create_backup(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.CreateBackupRequest import CreateBackupRequest
            params_dict = collect_user_args(self.app)
            req = CreateBackupRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域代码 """, dest='regionId', required=False)),
            (['--backup-id'], dict(help="""(string) 备份ID """, dest='backupId', required=True)),
            (['--file-name'], dict(help="""(string) MySQL：无需此参数；SQL Server：指定该备份中需要获取下载链接的文件名称，SQL Server必须输入该参数 """, dest='fileName', required=False)),
            (['--url-expiration-second'], dict(help="""(string) 指定下载链接的有效时间，单位秒,缺省为86400秒（即24小时） 取值范围：1-864000 """, dest='urlExpirationSecond', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取备份下载链接 ''',
        description='''
            获取备份下载链接。

            示例: jdc rds describe-backup-download-url  --backup-id xxx
        ''',
    )
    def describe_backup_download_url(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.DescribeBackupDownloadURLRequest import DescribeBackupDownloadURLRequest
            params_dict = collect_user_args(self.app)
            req = DescribeBackupDownloadURLRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 区域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--db-name'], dict(help="""(string) 数据库名称 """, dest='dbName', required=True)),
            (['--character-set-name'], dict(help="""(string) 字符集名称,mysql字符集包括：utf8；SQL Server字符集包括：Chinese_PRC_CI_AS、Chinese_PRC_CS_AS、SQL_Latin1_General_CP1_CI_AS、SQL_Latin1_General_CP1_CS_AS、Chinese_PRC_BIN """, dest='characterSetName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建数据库 ''',
        description='''
            创建数据库。

            示例: jdc rds create-database  --instance-id xxx --db-name xxx --character-set-name xxx
        ''',
    )
    def create_database(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.CreateDatabaseRequest import CreateDatabaseRequest
            params_dict = collect_user_args(self.app)
            req = CreateDatabaseRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 区域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--db-name'], dict(help="""(string) 库名称 """, dest='dbName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除数据库 ''',
        description='''
            删除数据库。

            示例: jdc rds delete-database  --instance-id xxx --db-name xxx
        ''',
    )
    def delete_database(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.DeleteDatabaseRequest import DeleteDatabaseRequest
            params_dict = collect_user_args(self.app)
            req = DeleteDatabaseRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 区域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--db-name'], dict(help="""(string) 库名称 """, dest='dbName', required=True)),
            (['--backup-id'], dict(help="""(string) 备份ID """, dest='backupId', required=True)),
            (['--backup-file-name'], dict(help="""(string) 指定该备份中用于恢复数据库的文件名称 """, dest='backupFileName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 从云数据库SQL Server备份中恢复单个数据库 ''',
        description='''
            从云数据库SQL Server备份中恢复单个数据库。

            示例: jdc rds restore-database-from-backup  --instance-id xxx --db-name xxx --backup-id xxx --backup-file-name xxx
        ''',
    )
    def restore_database_from_backup(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.RestoreDatabaseFromBackupRequest import RestoreDatabaseFromBackupRequest
            params_dict = collect_user_args(self.app)
            req = RestoreDatabaseFromBackupRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 区域代码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--db-name'], dict(help="""(string) 库名称 """, dest='dbName', required=True)),
            (['--shared-file-gid'], dict(help="""(string) 共享文件的全局ID，可从上传文件查询接口describeImportFiles获取；如果该文件不是共享文件，则全局ID为空 """, dest='sharedFileGid', required=False)),
            (['--file-name'], dict(help="""(string) 用户在单库上云中上传的文件名称 """, dest='fileName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 从用户上传的备份文件中恢复SQL Server数据库 ''',
        description='''
            从用户上传的备份文件中恢复SQL Server数据库。

            示例: jdc rds restore-database-from-file  --instance-id xxx --db-name xxx --file-name xxx
        ''',
    )
    def restore_database_from_file(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.RestoreDatabaseFromFileRequest import RestoreDatabaseFromFileRequest
            params_dict = collect_user_args(self.app)
            req = RestoreDatabaseFromFileRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 区域编码 """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) 实例ID """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取单库上云文件列表 ''',
        description='''
            获取单库上云文件列表。

            示例: jdc rds describe-import-files  --instance-id xxx
        ''',
    )
    def describe_import_files(self):
        client_factory = ClientFactory('rds')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.rds.apis.DescribeImportFilesRequest import DescribeImportFilesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeImportFilesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['create-account','delete-account','grant-privilege','reset-password','describe-backups','create-backup','describe-backup-download-url','create-database','delete-database','restore-database-from-backup','restore-database-from-file','describe-import-files',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('rds', self.app.pargs.api)
        skeleton.show()
