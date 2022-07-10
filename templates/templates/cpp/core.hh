#ifndef {PROJECT}_CORE_HH_
# define {PROJECT}_CORE_HH_

# define {PROJECT}_BEGIN_NAMESPACE namespace {project} {{
# define {PROJECT}_END_NAMESPACE }}

namespace core {{

/** (MAJOR * 10000) + (MINOR * 100) + PATCH */
# define {PROJECT}_VERSION 100
# define MAJOR ({PROJECT}_VERSION / 10000)
# define MINOR (({PROJECT}_VERSION - (MAJOR * 10000)) / 100)
# define PATCH ({PROJECT}_VERSION - (MAJOR * 10000) - (MINOR * 100))

}}  // namespace core

#endif  // !{PROJECT}_CORE_HH_