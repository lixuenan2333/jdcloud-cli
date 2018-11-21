# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
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
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class IamController(BaseController):
    class Meta:
        label = 'iam'
        help = 'IAM API'
        description = '''
        iam cli 子命令，IAM相关接口。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/387/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--create-permission-info'], dict(help="""(createPermissionInfo) 权限信息 """, dest='createPermissionInfo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建策略 ''',
        description='''
            创建策略。

            示例: jdc iam create-permission  --create-permission-info {"":""}
        ''',
    )
    def create_permission(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.CreatePermissionRequest import CreatePermissionRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreatePermissionRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--permission-id'], dict(help="""(int) 权限id """, dest='permissionId', type=int, required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询策略详情 ''',
        description='''
            查询策略详情。

            示例: jdc iam describe-permission-detail  --permission-id 5
        ''',
    )
    def describe_permission_detail(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.DescribePermissionDetailRequest import DescribePermissionDetailRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribePermissionDetailRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--permission-id'], dict(help="""(int) 权限id """, dest='permissionId', type=int, required=True)),
            (['--update-permission-info'], dict(help="""(updatePermissionInfo) 权限信息 """, dest='updatePermissionInfo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改策略 ''',
        description='''
            修改策略。

            示例: jdc iam update-permission  --permission-id 5 --update-permission-info {"":""}
        ''',
    )
    def update_permission(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.UpdatePermissionRequest import UpdatePermissionRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdatePermissionRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--page-number'], dict(help="""(int) 页码 """, dest='pageNumber', type=int, required=True)),
            (['--page-size'], dict(help="""(int) 每页显示数目 """, dest='pageSize', type=int, required=True)),
            (['--keyword'], dict(help="""(string) 关键字 """, dest='keyword',  required=False)),
            (['--query-type'], dict(help="""(int) 权限类型,0-全部，1-系统权限，2-自定义权限 """, dest='queryType', type=int, required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询策略列表 ''',
        description='''
            查询策略列表。

            示例: jdc iam describe-permissions  --page-number 0 --page-size 0 --query-type 0
        ''',
    )
    def describe_permissions(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.DescribePermissionsRequest import DescribePermissionsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribePermissionsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--sub-user'], dict(help="""(string) 子用户用户名 """, dest='subUser',  required=True)),
            (['--page-number'], dict(help="""(int) 页码 """, dest='pageNumber', type=int, required=True)),
            (['--page-size'], dict(help="""(int) 每页显示数目 """, dest='pageSize', type=int, required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询子用户策略列表 ''',
        description='''
            查询子用户策略列表。

            示例: jdc iam describe-sub-user-permissions  --sub-user xxx --page-number 0 --page-size 0
        ''',
    )
    def describe_sub_user_permissions(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.DescribeSubUserPermissionsRequest import DescribeSubUserPermissionsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeSubUserPermissionsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--sub-user'], dict(help="""(string) 子用户用户名 """, dest='subUser',  required=True)),
            (['--add-permissions-info'], dict(help="""(addPermissionsInfo) 权限信息 """, dest='addPermissionsInfo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 为子用户绑定策略 ''',
        description='''
            为子用户绑定策略。

            示例: jdc iam add-permissions-to-sub-user  --sub-user xxx --add-permissions-info {"":""}
        ''',
    )
    def add_permissions_to_sub_user(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.AddPermissionsToSubUserRequest import AddPermissionsToSubUserRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AddPermissionsToSubUserRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--permission-id'], dict(help="""(int) 权限id """, dest='permissionId', type=int, required=True)),
            (['--sub-user'], dict(help="""(string) 子用户用户名 """, dest='subUser',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 为子用户解绑策略 ''',
        description='''
            为子用户解绑策略。

            示例: jdc iam remove-permission-of-sub-user  --permission-id 5 --sub-user xxx
        ''',
    )
    def remove_permission_of_sub_user(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.RemovePermissionOfSubUserRequest import RemovePermissionOfSubUserRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = RemovePermissionOfSubUserRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--get-session-token-info'], dict(help="""(getSessionTokenInfo) 获取sessionToken参数 """, dest='getSessionTokenInfo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取SessionToken ''',
        description='''
            获取SessionToken。

            示例: jdc iam get-session-token  --get-session-token-info {"":""}
        ''',
    )
    def get_session_token(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.GetSessionTokenRequest import GetSessionTokenRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetSessionTokenRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--verify-session-token-info'], dict(help="""(verifySessionTokenInfo) 验证sessionToken参数 """, dest='verifySessionTokenInfo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 验证SessionToken有效性 ''',
        description='''
            验证SessionToken有效性。

            示例: jdc iam verify-session-token  --verify-session-token-info {"":""}
        ''',
    )
    def verify_session_token(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.VerifySessionTokenRequest import VerifySessionTokenRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = VerifySessionTokenRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--create-sub-user-info'], dict(help="""(createSubUserInfo) 子账号信息 """, dest='createSubUserInfo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建子账号 ''',
        description='''
            创建子账号。

            示例: jdc iam create-subuser  --create-sub-user-info {"":""}
        ''',
    )
    def create_subuser(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.CreateSubuserRequest import CreateSubuserRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateSubuserRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询AccessKey列表 ''',
        description='''
            查询AccessKey列表。

            示例: jdc iam describe-user-access-keys 
        ''',
    )
    def describe_user_access_keys(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.DescribeUserAccessKeysRequest import DescribeUserAccessKeysRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeUserAccessKeysRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建AccessKey ''',
        description='''
            创建AccessKey。

            示例: jdc iam create-user-access-key 
        ''',
    )
    def create_user_access_key(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.CreateUserAccessKeyRequest import CreateUserAccessKeyRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateUserAccessKeyRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--access-key'], dict(help="""(string) accessKey """, dest='accessKey',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 启用AccessKey ''',
        description='''
            启用AccessKey。

            示例: jdc iam enabled-user-access-key  --access-key xxx
        ''',
    )
    def enabled_user_access_key(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.EnabledUserAccessKeyRequest import EnabledUserAccessKeyRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = EnabledUserAccessKeyRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--access-key'], dict(help="""(string) accessKey """, dest='accessKey',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 禁用AccessKey ''',
        description='''
            禁用AccessKey。

            示例: jdc iam disabled-user-access-key  --access-key xxx
        ''',
    )
    def disabled_user_access_key(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.DisabledUserAccessKeyRequest import DisabledUserAccessKeyRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DisabledUserAccessKeyRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--access-key'], dict(help="""(string) accessKey """, dest='accessKey',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除AccessKey ''',
        description='''
            删除AccessKey。

            示例: jdc iam delete-user-access-key  --access-key xxx
        ''',
    )
    def delete_user_access_key(self):
        client_factory = ClientFactory('iam')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.iam.apis.DeleteUserAccessKeyRequest import DeleteUserAccessKeyRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteUserAccessKeyRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['create-permission','describe-permission-detail','update-permission','describe-permissions','describe-sub-user-permissions','add-permissions-to-sub-user','remove-permission-of-sub-user','get-session-token','verify-session-token','create-subuser','describe-user-access-keys','create-user-access-key','enabled-user-access-key','disabled-user-access-key','delete-user-access-key',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('iam', self.app.pargs.api)
        skeleton.show()
