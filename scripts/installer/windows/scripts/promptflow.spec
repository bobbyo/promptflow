# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

datas = [('../resources/CLI_LICENSE.rtf', '.'), ('../../../../src/promptflow/NOTICE.txt', '.'),
('../../../../src/promptflow/promptflow/_sdk/data/executable/', './promptflow/_sdk/data/executable/'),
('../../../../src/promptflow-tools/promptflow/tools/', './promptflow/tools/'),
('./pf.bat', '.'), ('./pfs.bat', '.'), ('./pfazure.bat', '.'), ('./pfsvc.bat', '.')]


packages = ['certifi', 'opentelemetry-sdk', 'six', 'Jinja2', 'Flask', 'ruamel.yaml', 'azure-ai-ml', 'Werkzeug', 'streamlit-quill', 'msal-extensions', 'httpx', 'isodate', 'bs4', 'blinker', 'opencensus-ext-azure', 'pandas', 'tabulate', 'pyinstaller', 'jaraco.classes', 'pydantic', 'typing-extensions', 'azure-mgmt-core', 'opentelemetry-proto', 'waitress', 'opentelemetry-exporter-otlp-proto-common', 'fixedint', 'fastapi', 'tornado', 'msal', 'streamlit', 'openai', 'pyrsistent', 'azureml-ai-monitoring', 'toml', 'pyjwt', 'keyring', 'altgraph', 'setuptools', 'numpy', 'cryptography', 'jsonschema', 'beautifulsoup4', 'pefile', 'azure-common', 'starlette', 'deprecated', 'msrest', 'gitpython', 'tqdm', 'opentelemetry-exporter-otlp-proto-http', 'pydeck', 'azure-storage-blob', 'flask-cors', 'tenacity', 'validators', 'werkzeug', 'flask', 'altair', 'sniffio', 'pyyaml', 'azure-cosmos', 'pyarrow', 'flask-restx', 'itsdangerous', 'pyinstaller-hooks-contrib', 'psutil', 'watchdog', 'gitdb', 'strictyaml', 'pywin32-ctypes', 'opentelemetry-api', 'ruamel.yaml.clib', 'azure-identity', 'greenlet', 'azure-monitor-opentelemetry-exporter', 'idna', 'filetype', 'rich', 'distro', 'docutils', 'attrs', 'python-dotenv', 'python-dateutil', 'tiktoken', 'azure-storage-file-share', 'tzlocal', 'azure-core', 'pillow', 'backoff', 'protobuf', 'click', 'cachetools', 'packaging', 'importlib-metadata', 'filelock', 'marshmallow', 'httpcore', 'azure-storage-file-datalake', 'regex', 'pydash', 'importlib-resources', 'googleapis-common-protos', 'sqlalchemy', 'aniso8601', 'colorama', 'cffi', 'pytz', 'requests', 'anyio']

for package in packages:
    datas += copy_metadata(package)
    datas += collect_data_files(package)

datas += collect_data_files('promptflow')
datas += copy_metadata('promptflow')
hidden_imports = [win32timezone', 'promptflow'] + ['certifi', 'opentelemetry.sdk', 'six', 'Jinja2', 'Flask', 'ruamel.yaml', 'azure.ai.ml', 'Werkzeug', 'streamlit_quill', 'msal.extensions', 'httpx', 'isodate', 'bs4', 'blinker', 'opencensus.ext.azure', 'pandas', 'tabulate', 'pyinstaller', 'jaraco.classes', 'pydantic', 'typing.extensions', 'azure.mgmt.core', 'opentelemetry.proto', 'waitress', 'opentelemetry.exporter.otlp.proto.common', 'fixedint', 'fastapi', 'tornado', 'msal', 'streamlit', 'openai', 'pyrsistent', 'azureml.ai.monitoring', 'toml', 'pyjwt', 'keyring', 'altgraph', 'setuptools', 'numpy', 'cryptography', 'jsonschema', 'beautifulsoup4', 'pefile', 'azure.common', 'starlette', 'deprecated', 'msrest', 'gitpython', 'tqdm', 'opentelemetry.exporter.otlp.proto.http', 'pydeck', 'azure.storage.blob', 'flask.cors', 'tenacity', 'validators', 'werkzeug', 'flask', 'altair', 'sniffio', 'pyyaml', 'azure.cosmos', 'pyarrow', 'flask.restx', 'itsdangerous', 'pyinstaller.hooks.contrib', 'psutil', 'watchdog', 'gitdb', 'strictyaml', 'pywin32.ctypes', 'opentelemetry.api', 'ruamel.yaml.clib', 'azure.identity', 'greenlet', 'azure.monitor.opentelemetry.exporter', 'idna', 'filetype', 'rich', 'distro', 'docutils', 'attrs', 'python.dotenv', 'python.dateutil', 'tiktoken', 'azure.storage.file.share', 'tzlocal', 'azure.core', 'pillow', 'backoff', 'protobuf', 'click', 'cachetools', 'packaging', 'importlib.metadata', 'filelock', 'marshmallow', 'httpcore', 'azure.storage.file.datalake', 'regex', 'pydash', 'importlib.resources', 'googleapis.common.protos', 'sqlalchemy', 'aniso8601', 'colorama', 'cffi', 'pytz', 'requests', 'anyio']

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
