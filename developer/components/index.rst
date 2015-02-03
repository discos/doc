.. _nuraghe-components:
 
######################
Nuraghe components API
######################

.. topic:: Abstract
    
   Nuraghe is designed following a software architectural pattern called
   *component-container model*. During the normal execution, the `ACS framework
   <http://www.eso.org/projects/alma/develop/acs/>`_ runs 10xx Nuraghe
   components, each one has in charge a specific hardware management (control 
   and monitoring). The goal of this document is to comprehensively explain 
   the APIs of some Nuraghe components (CLARIFY: ExternalClient because 
   currently is the only one that provides an ACS-independent Nuraghe 
   interface, but also other component that we want to explain the API since
   thier non-trivial configuration).


Contents:

.. toctree::
   :maxdepth: 1

   DewarPositioner/index.rst

