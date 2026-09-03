from setuptools import find_namespace_packages, setup


if __name__ == '__main__':
    setup(
        name='surrol',
        version='0.2.0.post1',
        description='SurRoL: An Open-source Reinforcement Learning Centered and '
                    'dVRK Compatible Platform for Surgical Robot Learning',
        author='Med-AIR@CUHK',
        keywords='simulation, medical robotics, dVRK, reinforcement learning',
        packages=find_namespace_packages(include=['surrol', 'surrol.*']),
        include_package_data=True,
        python_requires = '>=3.7',
        install_requires=[
            "gym>=0.15.6",
            "numpy>=1.21.1",
            "scipy",
            "pandas",
            "imageio",
            "imageio-ffmpeg",
            "opencv-python",
            "pybullet>=3.2.7",
            "roboticstoolbox-python==1.1.1",
            "spatialgeometry<1.4",
            "sympy",
            "trimesh",
        ],
        extras_require={
            "gui": [
                "panda3d==1.10.11",
                "kivymd",
            ],
            # optional dependencies, required by evaluation, test, etc.
            "all": [
                "tensorflow-gpu==1.14",
                "baselines",
                "mpi4py",  # important for ddpg
                "ipython",
                "jupyter",
            ]
        }
    )
    
