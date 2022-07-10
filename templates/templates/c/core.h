#ifndef {PROJECT}_CORE_H_
# define {PROJECT}_CORE_H_

/** (MAJOR * 10000) + (MINOR * 100) + PATCH */
# define {PROJECT}_VERSION 100

  struct {Project}VersionInfo {{
    const int major;
    const int minor;
    const int patch;
  }};

  const struct {Project}VersionInfo {project}_version_info = {{
    .major = ({PROJECT}_VERSION / 10000),
    .minor = (({PROJECT}_VERSION - (MAJOR * 10000)) / 100),
    .patch = ({PROJECT}_VERSION - (MAJOR * 10000) - (MINOR * 100))
  }}

#endif  // !{PROJECT}_CORE_H_
