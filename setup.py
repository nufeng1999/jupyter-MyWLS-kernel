from setuptools import setup

setup(name='jupyter_MyWLS_kernel',
      version='0.0.1',
      description='Minimalistic vbscript kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyWLS-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyWLS-kernel/tarball/0.0.1',
      packages=['jupyter_MyWLS_kernel'],
      scripts=['jupyter_MyWLS_kernel/install_MyWLS_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'wls','Wolfram','WolframScript','Mathematica'],
      include_package_data=True
      )
