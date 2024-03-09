# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_all
from PyInstaller.utils.hooks import copy_metadata

datas = [('../resources/CLI_LICENSE.rtf', '.'), ('../../../../src/promptflow/NOTICE.txt', '.'),
('../../../../src/promptflow/promptflow/_sdk/data/executable/', './promptflow/_sdk/data/executable/'),
('../../../../src/promptflow-tools/promptflow/tools/', './promptflow/tools/'),
('./pf.bat', '.'), ('./pfs.bat', '.'), ('./pfazure.bat', '.'), ('./pfsvc.bat', '.')]


all_packages = ['cryptography', 'requests', 'werkzeug', 'setuptools', 'altair', 'pydantic', 'streamlit', 'numpy', 'msal', 'pefile', 'python-dotenv', 'rich', 'pillow', 'typing-extensions', 'azure-cosmos', 'azure-storage-blob', 'psutil', 'strictyaml', 'cffi', 'azure-core', 'backoff', 'ruamel.yaml.clib', 'jsonschema', 'certifi', 'aniso8601', 'azure-monitor-opentelemetry-exporter', 'filetype', 'pytz', 'openai', 'colorama', 'gitpython', 'beautifulsoup4', 'pyyaml', 'fastapi', 'msrest', 'pyinstaller', 'attrs', 'pydash', 'altgraph', 'azure-storage-file-share', 'validators', 'opentelemetry-exporter-otlp-proto-http', 'docutils', 'pandas', 'azure-ai-ml', 'regex', 'azure-mgmt-core', 'filelock', 'marshmallow', 'Jinja2', 'azure-storage-file-datalake', 'waitress', 'httpx', 'pyjwt', 'six', 'deprecated', 'tornado', 'python-dateutil', 'opencensus-ext-azure', 'azure-common', 'pywin32-ctypes', 'opentelemetry-sdk', 'googleapis-common-protos', 'distro', 'cachetools', 'opentelemetry-proto', 'httpcore', 'sqlalchemy', 'ruamel.yaml', 'Werkzeug', 'blinker', 'gitdb', 'bs4', 'fixedint', 'sniffio', 'jaraco.classes', 'tenacity', 'isodate', 'packaging', 'tzlocal', 'importlib-metadata', 'Flask', 'pyrsistent', 'toml', 'tiktoken', 'itsdangerous', 'opentelemetry-api', 'flask-cors', 'flask-restx', 'tabulate', 'azureml-ai-monitoring', 'pydeck', 'pyinstaller-hooks-contrib', 'protobuf', 'streamlit-quill', 'importlib-resources', 'pyarrow', 'opentelemetry-exporter-otlp-proto-common', 'flask', 'azure-identity', 'tqdm', 'anyio', 'starlette', 'msal-extensions', 'idna', 'greenlet', 'watchdog', 'click', 'keyring']
meta_packages = ['cryptography', 'requests', 'werkzeug', 'setuptools', 'altair', 'pydantic', 'streamlit', 'numpy', 'msal', 'pefile', 'python-dotenv', 'rich', 'pillow', 'typing-extensions', 'azure-cosmos', 'azure-storage-blob', 'psutil', 'strictyaml', 'cffi', 'azure-core', 'ruamel.yaml.clib', 'jsonschema', 'certifi', 'aniso8601', 'azure-monitor-opentelemetry-exporter', 'filetype', 'pytz', 'openai', 'colorama', 'gitpython', 'beautifulsoup4', 'pyyaml', 'fastapi', 'msrest', 'pyinstaller', 'attrs', 'pydash', 'altgraph', 'azure-storage-file-share', 'opentelemetry-exporter-otlp-proto-http', 'docutils', 'pandas', 'azure-ai-ml', 'regex', 'azure-mgmt-core', 'filelock', 'marshmallow', 'Jinja2', 'azure-storage-file-datalake', 'waitress', 'httpx', 'pyjwt', 'six', 'deprecated', 'tornado', 'python-dateutil', 'opencensus-ext-azure', 'azure-common', 'pywin32-ctypes', 'opentelemetry-sdk', 'googleapis-common-protos', 'distro', 'cachetools', 'opentelemetry-proto', 'httpcore', 'sqlalchemy', 'ruamel.yaml', 'Werkzeug', 'blinker', 'gitdb', 'bs4', 'fixedint', 'sniffio', 'jaraco.classes', 'tenacity', 'isodate', 'packaging', 'importlib-metadata', 'Flask', 'toml', 'tiktoken', 'itsdangerous', 'opentelemetry-api', 'flask-cors', 'flask-restx', 'tabulate', 'azureml-ai-monitoring', 'pydeck', 'pyinstaller-hooks-contrib', 'protobuf', 'streamlit-quill', 'importlib-resources', 'pyarrow', 'opentelemetry-exporter-otlp-proto-common', 'flask', 'azure-identity', 'tqdm', 'anyio', 'starlette', 'msal-extensions', 'idna', 'greenlet', 'watchdog', 'click', 'keyring']

for package in all_packages:
    datas += collect_data_files(package)

for package in meta_packages:
    datas += copy_metadata(package)

opentelemetry_datas, opentelemetry_binaries, opentelemetry_hiddenimports = collect_all('opentelemetry')
data += opentelemetry_datas
datas += collect_data_files('streamlit_quill')
datas += collect_data_files('promptflow')
datas += copy_metadata('promptflow')
hidden_imports = ['win32timezone', 'promptflow', 'opentelemetry.context.contextvars_context'] + ['cryptography', 'requests', 'werkzeug', 'setuptools', 'altair', 'pydantic', 'streamlit', 'numpy', 'msal', 'pefile', 'python.dotenv', 'rich', 'pillow', 'typing.extensions', 'azure.cosmos', 'azure.storage.blob', 'psutil', 'strictyaml', 'cffi', 'azure.core', 'backoff', 'ruamel.yaml.clib', 'jsonschema', 'certifi', 'aniso8601', 'azure.monitor.opentelemetry.exporter', 'filetype', 'pytz', 'openai', 'colorama', 'gitpython', 'beautifulsoup4', 'pyyaml', 'fastapi', 'msrest', 'pyinstaller', 'attrs', 'pydash', 'altgraph', 'validators', 'opentelemetry.exporter.otlp.proto.http', 'docutils', 'pandas', 'azure.ai.ml', 'regex', 'azure.mgmt.core', 'filelock', 'marshmallow', 'jinja2', 'waitress', 'httpx', 'pyjwt', 'six', 'deprecated', 'tornado', 'python.dateutil', 'opencensus.ext.azure', 'azure.common', 'pywin32.ctypes', 'opentelemetry.sdk', 'googleapis.common.protos', 'distro', 'cachetools', 'opentelemetry.proto', 'httpcore', 'sqlalchemy', 'ruamel.yaml', 'werkzeug', 'blinker', 'gitdb', 'bs4', 'fixedint', 'sniffio', 'jaraco.classes', 'tenacity', 'isodate', 'packaging', 'tzlocal', 'importlib.metadata', 'flask', 'pyrsistent', 'toml', 'tiktoken', 'itsdangerous', 'opentelemetry.api', 'flask_cors', 'flask_restx', 'tabulate', 'azureml.ai.monitoring', 'pydeck', 'pyinstaller.hooks.contrib', 'protobuf', 'streamlit_quill', 'importlib.resources', 'pyarrow', 'opentelemetry.exporter.otlp.proto.common', 'flask', 'azure.identity', 'tqdm', 'anyio', 'starlette', 'msal.extensions', 'idna', 'greenlet', 'watchdog', 'click', 'keyring', 'azure.storage.fileshare', 'azure.storage.filedatalake']

hidden_imports += opentelemetry_hiddenimports
binaries = []
binaries += opentelemetry_binaries

block_cipher = None

pfcli_a = Analysis(
    ['pfcli.py'],
    pathex=[],
    binaries=binaries,
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
