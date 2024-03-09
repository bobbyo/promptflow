# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [('../resources/CLI_LICENSE.rtf', '.'), ('../../../../src/promptflow/NOTICE.txt', '.'),
('../../../../src/promptflow/promptflow/_sdk/data/executable/', './promptflow/_sdk/data/executable/'),
('../../../../src/promptflow-tools/promptflow/tools/', './promptflow/tools/'),
('./pf.bat', '.'), ('./pfs.bat', '.'), ('./pfazure.bat', '.'), ('./pfsvc.bat', '.')]


all_packages = ['filetype', 'pydeck', 'watchdog', 'opentelemetry-api', 'pyarrow', 'tenacity', 'gitdb', 'msal', 'toml', 'pyjwt', 'typing-extensions', 'pandas', 'pydantic', 'cffi', 'tornado', 'pywin32-ctypes', 'sniffio', 'ruamel.yaml', 'flask', 'certifi', 'msal-extensions', 'psutil', 'opencensus-ext-azure', 'pyrsistent', 'cryptography', 'starlette', 'importlib-resources', 'httpx', 'aniso8601', 'marshmallow', 'pyinstaller-hooks-contrib', 'cachetools', 'python-dotenv', 'protobuf', 'flask-restx', 'httpcore', 'rich', 'click', 'gitpython', 'altgraph', 'idna', 'streamlit-quill', 'pillow', 'backoff', 'python-dateutil', 'werkzeug', 'docutils', 'azure-monitor-opentelemetry-exporter', 'tzlocal', 'azureml-ai-monitoring', 'Werkzeug', 'openai', 'validators', 'pyyaml', 'filelock', 'deprecated', 'isodate', 'beautifulsoup4', 'packaging', 'tqdm', 'azure-storage-blob', 'regex', 'azure-mgmt-core', 'blinker', 'opentelemetry-proto', 'altair', 'opentelemetry-exporter-otlp-proto-common', 'Jinja2', 'streamlit', 'six', 'azure-cosmos', 'opentelemetry-sdk', 'colorama', 'fastapi', 'tiktoken', 'opentelemetry-exporter-otlp-proto-http', 'ruamel.yaml.clib', 'sqlalchemy', 'jaraco.classes', 'bs4', 'importlib-metadata', 'itsdangerous', 'pydash', 'greenlet', 'anyio', 'azure-storage-file-share', 'pytz', 'requests', 'googleapis-common-protos', 'azure-storage-file-datalake', 'pefile', 'Flask', 'azure-common', 'numpy', 'waitress', 'azure-core', 'keyring', 'jsonschema', 'azure-identity', 'pyinstaller', 'msrest', 'distro', 'tabulate', 'fixedint', 'strictyaml', 'azure-ai-ml', 'attrs', 'flask-cors', 'setuptools']
meta_packages = ['filetype', 'pydeck', 'watchdog', 'opentelemetry-api', 'pyarrow', 'tenacity', 'gitdb', 'msal', 'toml', 'pyjwt', 'typing-extensions', 'pandas', 'pydantic', 'cffi', 'tornado', 'pywin32-ctypes', 'sniffio', 'ruamel.yaml', 'flask', 'certifi', 'msal-extensions', 'psutil', 'opencensus-ext-azure', 'cryptography', 'starlette', 'importlib-resources', 'httpx', 'aniso8601', 'marshmallow', 'pyinstaller-hooks-contrib', 'cachetools', 'python-dotenv', 'protobuf', 'flask-restx', 'httpcore', 'rich', 'click', 'gitpython', 'altgraph', 'idna', 'streamlit-quill', 'pillow', 'python-dateutil', 'werkzeug', 'docutils', 'azure-monitor-opentelemetry-exporter', 'azureml-ai-monitoring', 'Werkzeug', 'openai', 'pyyaml', 'filelock', 'deprecated', 'isodate', 'beautifulsoup4', 'packaging', 'tqdm', 'azure-storage-blob', 'regex', 'azure-mgmt-core', 'blinker', 'opentelemetry-proto', 'altair', 'opentelemetry-exporter-otlp-proto-common', 'Jinja2', 'streamlit', 'six', 'azure-cosmos', 'opentelemetry-sdk', 'colorama', 'fastapi', 'tiktoken', 'opentelemetry-exporter-otlp-proto-http', 'ruamel.yaml.clib', 'sqlalchemy', 'jaraco.classes', 'bs4', 'importlib-metadata', 'itsdangerous', 'pydash', 'greenlet', 'anyio', 'azure-storage-file-share', 'pytz', 'requests', 'googleapis-common-protos', 'azure-storage-file-datalake', 'pefile', 'Flask', 'azure-common', 'numpy', 'waitress', 'azure-core', 'keyring', 'jsonschema', 'azure-identity', 'pyinstaller', 'msrest', 'distro', 'tabulate', 'fixedint', 'strictyaml', 'azure-ai-ml', 'attrs', 'flask-cors', 'setuptools']

for package in all_packages:
    datas += collect_data_files(package)

for package in meta_packages:
    datas += copy_metadata(package)

datas += collect_data_files('promptflow')
datas += copy_metadata('promptflow')
hidden_imports = ['win32timezone', 'promptflow'] + ['filetype', 'pydeck', 'watchdog', 'opentelemetry.api', 'pyarrow', 'tenacity', 'gitdb', 'msal', 'toml', 'pyjwt', 'typing.extensions', 'pandas', 'pydantic', 'cffi', 'tornado', 'pywin32.ctypes', 'sniffio', 'ruamel.yaml', 'flask', 'certifi', 'msal.extensions', 'psutil', 'opencensus.ext.azure', 'pyrsistent', 'cryptography', 'starlette', 'importlib.resources', 'httpx', 'aniso8601', 'marshmallow', 'pyinstaller.hooks.contrib', 'cachetools', 'python.dotenv', 'protobuf', 'flask.restx', 'httpcore', 'rich', 'click', 'gitpython', 'altgraph', 'idna', 'streamlit_quill', 'pillow', 'backoff', 'python.dateutil', 'werkzeug', 'docutils', 'azure.monitor.opentelemetry.exporter', 'tzlocal', 'azureml.ai.monitoring', 'Werkzeug', 'openai', 'validators', 'pyyaml', 'filelock', 'deprecated', 'isodate', 'beautifulsoup4', 'packaging', 'tqdm', 'azure.storage.blob', 'regex', 'azure.mgmt.core', 'blinker', 'opentelemetry.proto', 'altair', 'opentelemetry.exporter.otlp.proto.common', 'Jinja2', 'streamlit', 'six', 'azure.cosmos', 'opentelemetry.sdk', 'colorama', 'fastapi', 'tiktoken', 'opentelemetry.exporter.otlp.proto.http', 'ruamel.yaml.clib', 'sqlalchemy', 'jaraco.classes', 'bs4', 'importlib.metadata', 'itsdangerous', 'pydash', 'greenlet', 'anyio', 'azure.storage.file.share', 'pytz', 'requests', 'googleapis.common.protos', 'azure.storage.file.datalake', 'pefile', 'Flask', 'azure.common', 'numpy', 'waitress', 'azure.core', 'keyring', 'jsonschema', 'azure.identity', 'pyinstaller', 'msrest', 'distro', 'tabulate', 'fixedint', 'strictyaml', 'azure.ai.ml', 'attrs', 'flask.cors', 'setuptools']

block_cipher = None

pfcli_a = Analysis(
    ['pfcli.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pfcli_pyz = PYZ(pfcli_a.pure, pfcli_a.zipped_data, cipher=block_cipher)
pfcli_exe = EXE(
    pfcli_pyz,
    pfcli_a.scripts,
    [],
    exclude_binaries=True,
    name='pfcli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='.',
    icon='../resources/logo32.ico',
    version="./version_info.txt",
)

coll = COLLECT(
    pfcli_exe,
    pfcli_a.binaries,
    pfcli_a.zipfiles,
    pfcli_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='promptflow',
)
