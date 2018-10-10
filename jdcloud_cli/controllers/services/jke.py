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

import os
from argparse import RawTextHelpFormatter
from cement.ext.ext_argparse import expose
from jinja2 import Template
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class JkeController(BaseController):
    class Meta:
        label = 'jke'
        help = '使用该子命令操作jke相关资源'
        description = '''
        jke cli 子命令，可以使用该子命令操作jke相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/423/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--filters'], dict(help="""(array: filter) resourceTypes - 资源类型，暂时只支持[kubernetes];  """, dest='filters', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询(k8s 集群)配额 ''',
        description='''
            查询(k8s 集群)配额。

            示例: jdc jke describe-quotas 
        ''',
    )
    def describe_quotas(self):
        client_factory = ClientFactory('jke')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jke.apis.DescribeQuotasRequest import DescribeQuotasRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeQuotasRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-quotas',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('jke', self.app.pargs.api)
        skeleton.show()

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 ID """, dest='regionId', required=False)),
            (['--cluster-id'], dict(help="""(string) 集群 ID """, dest='clusterId', required=True)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取密钥凭证 ''',
        description='''
            获取密钥凭证。

            示例: jdc jke get-credential --cluster-id xxx
        ''',
    )
    def get_credential(self):
        client_factory = ClientFactory('jke')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jke.apis.DescribeClusterRequest import DescribeClusterRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeClusterRequest(params_dict, headers)
            resp = client.send(req)
            if resp.error is not None:
                Printer.print_result(resp)
            else:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                with open('%s/../../resources/jke/config.jinja' % current_dir) as f:
                    content = f.read()

                template = Template(content)
                result = template.render(self._build_credential_data(resp.result['cluster']))
                self._write_credential_file(result)
                Printer.print_text('Generate cluster credential successfully.')

        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e

    def _build_credential_data(self, cluster):
        masterAuth = cluster['masterAuth']
        return {
            'certificate_authority_data': masterAuth['clusterCaCertificate'],
            'server': 'https://%s:%s' % (cluster['endpoint'], cluster['endpointPort']),
            'username': masterAuth['user'],
            'password': masterAuth['password'],
            'client_certificate_data': masterAuth['clientCertificate'],
            'client_key_data': masterAuth['clientKey'],
            'context_name': 'cert-authentication@kubernetes' if cluster['clientCertificate'] else 'basic-authentication@kubernetes'
        }

    def _write_credential_file(self, content):
        home = os.getenv('HOME')
        kube_dir = '%s/.kube' % home
        if not os.path.exists(kube_dir):
            os.mkdir(kube_dir)

        with open('%s/config' % kube_dir, 'w') as f:
            f.write(content)