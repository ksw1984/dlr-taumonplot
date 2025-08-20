#********************************************************************************
#*                                                                              *
#*                            #####       #                                     *
#*                              #   ##### #                                     *
#*                              #   #     #                                     *
#*                              #   ###   #                                     *
#*                              #   #     #                                     *
#*                            ##### #     #####                                 *
#*                                  #                                           *
#*                                                                              *
#********************************************************************************
#*                                                                              *
#* This program is developed at the Institute of Aircraft Design & Lightweight  *
#* Structures at the Technical University of Braunschweig                       *
#*                                                                              *
#* This program is written in Python <= 2.7 under Windows and Linux             *
#* This program was updated to support Python 3.X                               *
#*                                                                              *
#* This program is distributed in the hope that it will be useful,              *
#* but WITHOUT ANY WARRANTY; without even the implied warranty of               *
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                         *
#*                                                                              *
#********************************************************************************
#*                                                                              *
#* written by          : S. Lender                                              *
#* modified by 	       : K. Sommerwerk                                           *
#* e-mail              : s.lender@tu-braunschweig.de                            *
#*                       k.sommerwerk@tu-braunschweig.de                        *
#* first implementation: 01.06.2013 (DD/MM/YYYY)                                *
#*                                                                              *
#********************************************************************************
#*                                                                              *
#* Revision history: version 1.00, 04.08.2013 	# working on WIN&LINUX          *
#*                                                                              *
#*                                                                              *
#*                                                                              *
#********************************************************************************
"""
Sphinx Documentation Generator

.. Note::
    deactivated :special-members: for sphinx version <= 1.1.0

.. todolist::   
   
"""
import os,sys, time, shutil	
import pickle as p
import platform         # for platform checks WIN/UNIX

import sphinx		# for version checks
sphinx_version = sphinx.__version__
print(f"-Using Sphinx version {sphinx_version}")

IFL_LOGO_PDF = "2010_Logo_IFL.png"
IFL_LOGO_HTML = "IFL_Logo_10.png"

def main():
    """
    .. available builders::

    ==========	===============================================================================================================================
    builder		description
    ==========	===============================================================================================================================
    html 		standard HTML builder
    epub 		html+generates an epub file for ebook readers
    latex  		LaTeX files in the output directory. Also directly executes pdflatex 3 times.
    singlehtml 	combines the whole project in one output file
    changes 	Usefull for ChangeLog file. HTML overview of all versionadded, versionchanged and deprecated directives for the current version
    linkcheck 	scans all documents for external links, tries to open them with urllib2, and writes an overview which ones are broken and redirected to standard output and to output.txt

    dirhtml 	directory with HTML files
    text  		text file for each reST file
    man 		manual pages in the groff format
    texinfo  	Texinfo files that can be processed into Info files by the makeinfo program
    pickle 		directory with pickle files containing mostly HTML fragments and TOC information
    json 		directory with JSON files containing mostly HTML fragments and TOC information
    gettext  	gettext-style message catalogs
    ==========	===============================================================================================================================
    """
    # ###############
    # BUILDER SETTINGS
    # ###############   
    # outputs=['html', 'latex','dirhtml', 'singlehtml','epub', 'text','man', 'texinfo']    # list of output formats
    # outputs=['html','singlehtml', 'latex']
    # outputs=['text','man','texinfo']
    outputs=['latex']
    #
    # ###############
    # DOCUMENTATION SETTINGS
    # ###############
    project_name='taumonplot'   # Name of the software project to be documented
    path_main='./../'                   # python-code-files to be documented are assumed here (normally the directory below)
    path_files_rst='./'                 # Path where user placed additional rst-files
    
    version='2.0'                        # version number
    release='2.0.5'                     # release number
    author='K. Sommerwerk'   # author name
    #~ author='Institute of Aircraft Design \& Lightweight Structures (IFL) & Technische Universitaet Braunschweig'
    files_py=['taumonplot']     # file names of src files to document
    #~ files_py=[]     # file names of src files to document
    files_py_members={}                 # if only certain mebers need to be documented. check Doc.
    files_rst=['disclaimer_author',
                'usage',
                'manual',
                'versions',
                'todo'
                ]                 # Names of additional rst files to be included. Usefull for requirements, user guide etc.
    #~ files_rst=[                      
                #~ ] 
    
    # ###############
    # EXECUTABLE PATHS
    # ###############
        
    if platform.system()  == "Linux":
        path_sphinx='/usr/bin/sphinx-build'         # which sphinx-build
        path_graphviz='/usr/bin/dot'                # which dot
        path_pdflatex='/usr/bin/pdflatex'           # which pdflatex (only necessary if latex in outputs)
       
    elif platform.system()  == "Windows":
        path_sphinx='C:/Python26/Scripts/sphinx-build.exe'    # which sphinx-build        
        path_graphviz='C:/Graphviz2.32/bin/dot.exe'           # which dot        
        path_pdflatex='C:/MiKTeX 2.9/miktex/bin/pdflatex'      # which pdflatex (only necessary if latex in outputs)
                
    else: 
        print(f"- ERROR: skript not configured for platform {platform.system()}. Check code and add platform type")
        raise
        
    # ###############
    # DOCUMENTATION PATHS (working with this configuration. There should not be a need to change this)
    # ###############    
    path_source='./source'                  # folder created where all files are put to generate documentation
    path_doctree=True                       # generate a doctree folder 
    path_sphinx_patterns="./"               # adds _static folder during execution
                     
    
    # ###############
    # OPTIONS LOGGER, DELETION ETC
    # ###############
    graph=True                              # Switch to include inheritance diagram. Graphiviz is necessary.
    if sphinx_version <= '1.1':
        graph=False                         # Graph not working. Error *.map file not found for graphviz manipulation.
    # log=True                                # Generate a log file
    log=False
    code_rst_header = None                  # Header of the documentation. Written into 'code.rst'
    # delete = False                          # Delete source folder
    delete = True      

    # ###############
    # Checks for paths
    # ###############
    
    if not os.path.isfile(path_sphinx):
        print( "- ERROR: path to sphinx-build not found. Check variable 'path_sphinx'!")
        raise
    if graph and not os.path.isfile(path_graphviz):
        print( "- ERROR: path to graphviz (dot) not found. Check variable 'path_graphviz'!")
        raise
    if 'latex' in outputs and not os.path.isfile(path_pdflatex):
        print( "- ERROR: path to pdflatex not found. Check variable 'path_pdflatex'!")
        raise
    if not os.path.isdir("./_static"):
        print( "- ERROR: folder './_static' missing. Copy the folder and place it in the same as this file!")
        raise
    
    #===============================================================================
    # GENERATOR
    #===============================================================================
    for output in outputs:
        print(f" --- Generating for output {output}")
        d = DocumentationSphinx(output=output,
                                project_name=project_name,
                                path_main=path_main,

                                #path_target=path_target,

                                path_source=path_source,
                                path_doctree=path_doctree,
                                path_files_rst=path_files_rst,

                                path_sphinx=path_sphinx,
                                path_graphviz=path_graphviz,
                                path_sphinx_patterns=path_sphinx_patterns,
                                path_pdflatex=path_pdflatex,

                                version=version,
                                release=release,
                                author=author,
                                files_py=files_py,
                                files_py_members=files_py_members,
                                files_rst=files_rst,
                                code_rst_header=code_rst_header,
                                graph = graph,
                                log=log,
                                delete=delete)
        d.autorun()
    #===============================================================================
    # \GENERATOR
    #===============================================================================
    #
#
class BaseObject:
    """
    This class contains basic methods and attributes. It is a general base class. 
    """
    def __init__(self,olvl=0,blank='  '):
        """
        generic initialization.
    
        :param olvl: starting indentation level. Handy if class is called by another instance;
            the indentation level of the caller can be taken
        :type olvl: integer
        :param blank: Standard indentation for output (default= ``'  '``)
        :type blank: string
        
        """
        
        self.o = olvl
        self.b = blank
    
    def op(self,o=1):
        """
        Increase of output indentation level.
        
        :param o: Incrementor of output indentation level (default=1)
        :type o: integer
        """
        
        self.o+=o
    
    def om(self,o:int=1):
        """
        Decrease of output indentation level.
        
        :param o: Decrementor of output indentation level (default=1)
        :type o: integer
        """
        self.o-=o
    
    def save(self, file_name):
        """
        Save instance with pickle.
        
        :param file_name: Name of the file
        :type file_name: string
        
        .. note::
            - If no absolute path is given, stores in ``'./'`` (just like pickle)
            - Use of file-extension is recommended (e.g. ``'.pck'``)
        
        """
        self.write(f"SAVE object as '{file_name}'")
        fout = open(file_name,'wb')
        p.dump(self, fout)
        fout.close()
        self.write("SAVING object finished")
    
    def write(self, string: str):
        """
        String which will be printed with indentation corresponding to current output level
        
        :param string: String which will be printed
        :type string: string
        
        Example::
            
            >>> foo.write("SAVING started")
            SAVING started
            >>> foo.op()
            >>> foo.write("Save under './test.pck'")
              Save under './test.pck'
        
        """
        
        print( self.o*self.b, string)

    @staticmethod
    def s_fmt(s:str):
        """
        Format input string for easier comparison regardless of Capitals or whitespaces
            - Remove whitespaces
            - No capital latters (turned to small)
        
        :param s: string to be treated
        :type s: string
        """
        return s.replace(' ','').lower()


class DocumentationSphinx(BaseObject):
    """
    This class contains all elements of a sphinx documentation.
    It gets necessary attributes, can set default values for optional values and controls the generation of the documentation.
    
    Author: S. Lender -
    Date: 18/04/2013 - (DD/MM/YYYY)
    Version: 1.
    Release: 1.1.0
    
    """
    def __init__(self, 
                    project_name=None, 
                    path_main=None, 
                    files_py=None,
                 author='anonymous',
                 code_rst_header=None,
                 files_rst=['code'],
                 files_py_members={},
                 graph=True,
                 output='html',
                 path_source='./source',
                 path_target=None,
                 path_doctree=False,
                 path_files_rst='./',
                 path_sphinx='C:/Program Files (x86)/sphinx/sphinx-build.py',
                 path_graphviz='C:/Program Files (x86)/Graphviz2.30/bin/dot.exe',
                 path_sphinx_patterns='E:/prog-vorlagen/Sphinx_Vorlagen',
                 path_pdflatex="C:/MiKTeX 2.9/miktex/bin/pdflatex",
                 version='1.',
                 release='1.0',
                 log=False,
                 delete=False,
                 olvl=0, blank='  '):
        """
        The given parameters are assigned to attributes of the same name.
        
        The parameters ``path_main``, ``project_name``, ``files_py`` are compulsory.
        For the other parameter *default values* are at hand that lead to a working set.
        
        :param project_name: Compulsory input. Name of the software project to be documented. 
            Will appear multiple in documentation. (default= ``None``)
        :type project_name: string
        
        :param path_main: Compulsory input. Main path to the project to be documented. 
            The python-code-files to be documented are assumed here. (default= ``None``)
        :type path_main: string
        
        :param files_py: Compulsory input. Python file(s) with source code.
            - List of strings (for multiple files)
            - String (only one file)
            The order of the files is preseved in the documentation (default=None)
        :type files_py: list,string
        
        
        :param author: Author(s) of the software project. (default= *'anonymous'*)
        :type author: string
        
        :param code_rst_header: Header of the documentation. Written into 'code.rst' (default= ``None``)
        :type code_rst_header: string
        
        :param files_rst: Additional rst-files. Must be stored in path_files_rst and will be copied to path_main/path_source.
            Inclusion into documentation is in order of appearance in list.
            If *'code.rst'* is not included it is always added. 'code.rst' is always set to the last position.
            - List of strings (for multiple files)
            - String (only one file)
            (default=[*'code'*])            
        :type files_rst: list,string
        
        :param files_py_members: dictionary that can specify if only certain members (functions, classe,...) 
            of a source-code file shall be included in the documentation. 
            Keys are the names of the corresponding source-code files like given in ``files_py``.
            (i.e. with of without file-extension) Make sure they match!
            For each key (=file) the included members can be stated.
            If nothing given or a file of ``files_py`` is not present in ``files_py_members`` all members
            are included in the documentation. (default= ``{}``)
        :type files_py_members: dict
        
        :param graph: Switch to include inheritance diagram. Graphiviz is necessary. (default= ``True``)
        :type graph: bool
        
        :param output: Output format. Common: *'html'*, *'singlehtml'*, *'latex'*,... 
            (for more see sphinx documentation or -source-code)
            (default= *'html'*)
        :type output: string
        
        :param path_source: Source path of sphinx. Sphinx looks for *'conf.py'* and additional rst-files here. 
            Will be generated if not present. Path relative to main path possible. (default= *'./source'*)
        :type path_source: string
        
        :param path_target: Path where sphinx builds the output.
            Will be generated if not present. Path relative to main path possible.
            Default is set in self.check_input_parameters()
            (default= ``'./build/<output>'``,  e.g. *'./build/html'*)
        :type path_target: string
        
        :param path_doctree: Path where the doctree-folder will be created with the ``'-d'`` flag.
            It can be used in subsequent runs. Value assignation in ``self.check_input_parameters()``.
            Path relative to main path possible. (default= ``False``)
            
            ========== ========================================
            Input      Action
            ========== ========================================
            ``None``   No explicit doctree folder
            ``False``  No explicit doctree folder
            ``True``   Set standard value (*'./build/doctree'*)
            *string*   Set input as path_doctree
            ========== ========================================
            
        :type path_doctree: string, bool
        
        :param path_files_rst: Path where user placed additional rst-files, if given by files_rst.
            Files will be copied to path_main/path_source. (default= './' = ``path_main``)
        :type path_files_rst: string
        
        :param path_sphinx: Path to the sphinx sphinx-bulid.py program. 
            (default= *'C:/Program Files (x86)/sphinx/sphinx-build.py'*)
        :type path_sphinx: string
        
        :param path_pdflatex: Path to the pdflatex executable. 
            (default= *'C:/MiKTeX 2.9/miktex/bin/pdflatex'*)
        :type path_sphinx: string        
        
        :param path_graphviz: Path to dot.exe of program Graphviz. Necessary for inheritance diagrams.
            (default= *'C:/Program Files (x86)/Graphviz2.30/bin/dot.exe'*)
        :type path_graphviz: string
        
        :param path_sphinx_patterns: Path to ready patterns of sphinx. Expects folder *'_static/'* here.
            IFL-Theme is stored here common for all documentations.
            Choice for other themes or default could be implemented but is not.
            (default= *'E:/prog-vorlagen/Sphinx_Vorlagen'*)
        :type path_sphinx_patterns: string
        
        :param version: Version of the software project. (default= *'1.'*)
        :type version: string
        
        :param release: Release of the software project. (default= *'1.0'*)
        :type release: string
        
        :param log: Name of the log-file where shell output is directed to.
            Log-file is always stored in path_target.
            Value assignation in ``self.check_input_parameters()``.
            (default= ``False``)
            
            ========== ================================
            Input      Action
            ========== ================================
            ``None``   No log-file
            ``False``  No log-file
            ``True``   Set standard value (``log.dat``)
            *string*   Set input log-file name
            ========== ================================
            
        :type log: string, bool
        :param delete: Switch to delete source-folder after built of documentation. (default= ``False``)
        :type delete: bool
        
        :param olvl: Level of display output indentation. Handy if called by another instance. (default=0)
        :type olvl: integer
        
        :param blank: Indentation string for display output. (default='  ')
        :type blank: string
        
        """
        
        BaseObject.__init__(self)
        
        
        # necessary input
        self.project_name = project_name
        self.path_main = path_main
        self.files_py = files_py
        
        # optional input, defaults work well
        self.author = author
        self.code_rst_header = code_rst_header
        self.files_rst = files_rst
        self.files_py_members = files_py_members
        self.graph = graph
        self.output = output
        self.path_source = path_source
        self.path_target  = path_target   # will be set to default in self.check_input_parameters()
        self.path_doctree = path_doctree  # will be set to default in self.check_input_parameters()
        self.path_files_rst = path_files_rst
        self.path_sphinx = path_sphinx
        self.path_graphviz = path_graphviz
        self.path_pdflatex = path_pdflatex
        self.path_sphinx_patterns = path_sphinx_patterns
        self.version = version
        self.release = release
        self.log = log
        self.delete = delete
        self.olvl = olvl
        self.blank = blank
                        
        
        # further possible input parameter but other values than index did not work
        self.master_doc = 'index'
    
    def autorun(self):
        """
        Executes all necesry steps.
        
        0. check input parameters
        1. create folder *'source/'*
        2. in folder source
            1. copy hereto from `path_sphinx_pattern` folder *'_static/'* with contents
            2. create empty folder *'_templates'*
            3. adapt and write file *`conf.py`* via ``Documentation_sphinx_conf_py_file.autorun()``
            4. write file *`code.rst`* via ``Documentation_sphinx_code_rst_file.autorun()``
               with possible header and desired options for source.files (inheritance diagram) 
               -> takes code files from ``files.py`` 
            5. add additional rst-textFiles if applicable -> need name of additional rst-textFiles
            6. write file *`index.rst`* via ``Documentation_sphinx_index_rst_file.autorun()``
        3. execute command line
        4. delete source-folder *(optional)*
        
        """
        
        self.write("- step 0 :")
        # 0. check input parameters
        if not self.check_input_parameters():
            print( '!!! ERROR: autorun aborted !!!')
            return
        
        self.write("- steps 1., 2.1, 2.2 :")
        # 1. create folder 'source'
        # 2. in folder source
        # 2.1. copy hereto folder '_static' with contents
        # 2.2. create empty folder '_templates'
        self.create_folder_structure()
        
        self.write("- step 2.3 :")
        # 2.3. adapt and write file 'conf.py'
        self.write_file_conf_py()
        
        self.write("- step 2.4 :")
        # 2.4. write file 'code.rst' --> needs all code files and their desired output
        self.write_file_code_rst()
        
        if len(self.files_rst) > 0:
            self.write("- step 2.5 :")
            # 2.5. add additional rst-textFiles if applicable --> need name of additional rst-textFiles
            self.add_additional_files_rst()
        
        self.write("- step 2.6 :")
        # 2.6. write file 'index.rst'
        self.write_file_index_rst()
        
        self.write("- step 3. :")
        # 3. execute command line
        self.execute_command_line()
        print( "Delete:",self.delete)
        if self.delete:
            self.write("- step 4. :")
            # 4. delete source-folder
            self.delete_source_folder()
            
            
        if self.output == "latex":  
            self.adapt_tex_document()
            
            texfile = f"{self.project_name}.tex"
            cwd = os.getcwd()
            
            os.chdir(self.path_target)      # change path to include all *cls files
            cmd = f"{self.path_pdflatex} {texfile}"

            for i in range(4):      # run pdflatex 3 times to have all links etc. resolved
                self.write(f"Execute command line: {cmd}")
                os.system(cmd)
            os.chdir(cwd)
    
    def adapt_tex_document(self):
        """
        adapts the *.tex document to allow line breaks in code and to fix the longtables to the page width
        """
        texfile = f"{self.project_name}.tex"
        #
        texfile = os.path.join(self.path_target,texfile)
        #
        f = open(texfile,'r')   # read *.tex file
        f_list = f.readlines()
        f.close()
        #
        f = open(texfile,'w')   # adapt *.tex file
        for line in f_list:
            
            if line.startswith("\\begin{longtable}{ll}"):   # limits the longtable width to columnwidth
    
                line = "\\begin{longtable}{p{0.45\\textwidth}p{0.50\\textwidth}}"                   
                f.writelines(line+"\n")
                          
            elif "\\code{" in line: # adaptation to allow line breaks in code \nolinkurl{...}                    
                                   
                # count = line.count("\code{")
                split = line.split("\code{")
                
                for sid, s in enumerate(split[1:]): # add additional } to first occurrence of } from \code{..}
                    for it, letter in enumerate(s):
                        if letter == "}":                                
                            split[sid+1] = s[:it]+"}"+s[it:]
                            break
                
                line = "\\code{\\nolinkurl{".join(split)    # add \nolinkurl{ to \code{
                f.writelines(line)                 
    
            else:
                f.writelines(line)           
            
            
            #~ \begin{tabulary}{\linewidth}{|l|l|}
        f.close()
            
            
        return
        
    def _get_path_absolute(self, path_relative):
        """
        Receives a path, checks if this path is relative and if,
        calls function ``convert_path_relative2absolute()`` to get an absolute path.
        Root path to the relative path is ``path_main``
        
        :Parameters:
            path_relative : string
                Arbitrary path, relative or absolute path, both possible 
        
        :Return:
            path_absolute : string
                   Absolute path of relative path to root path ``path_main``
        """
        
        # given path is absolute path
        if path_relative[0] != '.' and ':' in path_relative:
            path_absolute = path_relative
        
        else:
            self.write("relative path -> adaption necessary")
            #~ path_absolute = convert_path_relative2absolute(self.path_main, path_relative)            
            path_absolute = os.path.abspath(path_relative)
        
        return path_absolute
    
    
    
    def check_input_parameters(self):
        """
        Check and adapt input parameters:
        
        - Check presence of ``self.path_main`` -> Raise Error
        - Check presence of ``self.project_name`` -> Raise Error
        - Get absolute path for ``self.path_source`` if given relative path
        - Get absolute path for ``self.path_files_rst`` if given relative path
        - Get absolute path for ``self.path_sphinx_patterns`` if given relative path
        - Check ``self.path_target``
            - Set to given value
            - Set default value (``./build/<output>/``) if ``None`` given
            - Get absolute path if necessary (``path_main/build/<output>/``)
        - Check ``self.path_doctree``
            - Set to  given value
            - Set default value (``./build/doctree/``) if ``True`` given
            - Get absolute path if necessary (``path_main/build/doctree/``)
        - Check ``self.files_py``
            - Check presence -> Raise Error
            - Check if string -> convert to list
            - Check if list -> check if all members are strings
            - Remove file-extensions, if present
        - Check ``self.files_py_members``
            - remove file-extension
            - check if keys are in self.files.py
            - convert string values into lists
        - Check ``self.files_rst``
            - Check if string -> convert to list
            - Check if list -> check if all members are strings
            - Move to / Add at last place *'code'* (for *'code.rst'*)
        - Check ``self.log``
            - Set to given value
            - Set default value (``log.dat``) if ``True`` given
            - Get absolute path if necessary (``path_main/build/doctree/``)
        """
        self.write("CHECK input parameters")
        
        # self.path_main: main path of the source-files to be documented
        if not self.path_main:
            print( '!!! ERROR: need main path where python source-code is !!!')
            return False
        
        
        # self.project_name: name of the project to be documented
        if not self.project_name:
            print( '!!! ERROR: need project-name to document !!!')
            return False
        
        # check in pathes are relative pathes -> convert to absolute pathes
        self.path_main            = self._get_path_absolute(self.path_main)        
        sys.path.append( self.path_main )   # append to path        
        self.path_source          = self._get_path_absolute(self.path_source)
        self.path_files_rst       = self._get_path_absolute(self.path_files_rst)
        self.path_sphinx_patterns = self._get_path_absolute(self.path_sphinx_patterns)
        
        
        # self.path_target: name of the project to be documented
        # default is './build/'+self.output --> e.g. './build/html/'
        if not self.path_target:
            self.path_target = './build/'+self.output
        if self.path_target:
            #~ self.path_target = convert_path_relative2absolute(self.path_main, self.path_target)
            self.path_target = os.path.abspath(self.path_target)
        
        
        # self.path_doctree: path of the doctree-files
        if self.path_doctree:
            if self.path_doctree == True:
                self.path_doctree = './build/doctree'
            #~ self.path_doctree = convert_path_relative2absolute(self.path_main, self.path_doctree)
            self.path_doctree = os.path.abspath(self.path_doctree)
        
        # self.files_py: python source-files to be documented
        # - check if list and all members are strings and no file-extensions
        self.files_py = self._check_input_parameter_filelist(self.files_py, '.py')
        
        # - nothing or False values given
        #~ if not self.files_py:
            #~ print '!!! ERROR: need python source-files to document !!!'
            #~ return False
        
        # self.files_py_members: dictionary with exclusive members to be included for given files
        files_py = self.files_py_members.keys()
        for file_py in files_py:
            # - remove file-extension
            if file_py[-3:] == '.py':
                self.files_py_members[file_py[:-3]] = self.files_py_members[file_py]
                del self.files_py_members[file_py]
                file_py = file_py[:-3]
            # - check if keys are in self.files.py
            if file_py not in self.files_py:
                print( '!!! ERROR: source-code file in exclusive member selection (files_py_members) !!!')
                print( '!!!        is not given in list of source-code files (files_py)              !!!')
                return False
            # - convert string values into lists
            if type(self.files_py_members[file_py]).__name__ == 'str':
                self.files_py_members[file_py] = [self.files_py_members[file_py]]
        
        
        # self.files_rst: name of additional rst-files to be included plus code.rst
        # - explicitly 'None' given
        if not self.files_rst:
            self.files_rst = ['code']
        
        # - check if is list and all members are strings and no file-extensions
        self.files_rst = self._check_input_parameter_filelist(self.files_rst, '.rst')
        
        # - include code as last member
        try:
            i = self.files_rst.index('code')
            
            if i != len(self.files_rst)-1:
                del self.files_rst[i]
                self.files_rst.append('code')
        except Exception:
            self.files_rst.append('code')

        
        # set log-file name
        if self.log:
            if self.log == True:
                self.log = 'log.dat'
            
            self.log = os.path.join(self.path_target,self.log)

        
        self.write("CHECKING finished")
        return True

    @staticmethod
    def _check_input_parameter_filelist(filelist: str|list, extension:str):
        """
        Checks the input.
        """
        l = len(extension)
        
        # string given --> converted to list
        if type(filelist).__name__ == 'str':
            filelist = [filelist]
        
        # list given
        if type(filelist).__name__ == 'list':
            
            for i,file in enumerate(filelist):
                
                # - check for each member if string
                if type(file).__name__ == 'str':
                    # --- remove extension, e.g. '.py', if necessary
                    if file[-l:] == extension:
                        filelist[i] = file[:-l]
                
                # - raise error if no string
                else:
                    print (f"!!! ERROR: need {extension} source-files as list of strings (for multiple files) !!!")
                    return False
        
            return filelist
        
        else:
            print( f"!!! ERROR: need {extension} source-files as string (one file) or list of strings (multiple files) !!!" )
            return False

    def create_folder_structure(self):
        """
        Creates the necessary folder structure.
        
        1. create folder *'source/'*
        2. in folder source
            1. copy hereto from ``path_sphinx_pattern`` folder *'_static/'* with contents
            2. create empty folder *'_templates/'*
        """
        self.write("CREATE folder structure")
        self.op()
        
        # 1. create folder 'source'
        self.write(f"create source-directory: {self.path_source}")
        #~ cmd = 'mkdir %s' % adapt_string_for_dos(self.path_source)
        cmd = f"mkdir {self.path_source}"
        print( cmd)
        os.system(cmd)
        
        
        # 2. in folder source
        self.write("in folder source")

        # 2.1. copy hereto folder '_static' with contents
        self.write("2.1 copy hereto folder '_static' with contents from '{self.path_sphinx_patterns}'")
        #~ os.system('xcopy %s %s /e /c /i /h /k /y' \
                   #~ % (adapt_string_for_dos(self.path_sphinx_patterns + '/_static'), \
                      #~ adapt_string_for_dos(self.path_source + '/_static')))
        src = os.path.join(self.path_sphinx_patterns,'_static')
        dst = os.path.join(self.path_source,'_static')       
        print(src)
        print(dst)
        try:
            shutil.copytree(src,dst)
        except OSError as e:
            print (e)
        
        
        # 2.2. create empty folder '_templates'
        self.write("create empty folder '_templates'")
        #~ cmd = 'mkdir %s' % adapt_string_for_dos(self.path_source + '/_templates')
        cmd = 'mkdir %s' % (os.path.join(self.path_source,'_templates'))        
        print( cmd)
        os.system(cmd)
        
        self.om()
        self.write("CREATING finished")
    
    def write_file_conf_py(self):
        """
        Write file *`conf.py`* via ``Documentation_sphinx_conf_py_file.autorun()``.
        Options are taken from attributes which are set by ``self.__init__`` input variables 
        """
        
        conf_py_file = DocumentationSphinxConfPyFile(self.path_main, self.path_source, self.project_name, self.author,
                                                     self.version, self.release, self.master_doc, self.path_graphviz,
                                                     self.output, self.o)
        conf_py_file.autorun()
    
    def write_file_code_rst(self):
        """
        Write file *`code.rst`* via ``Documentation_sphinx_code_rst_file.autorun()``
        with possible header and desired options for source-code files (inheritance diagram) 
        -> takes source-code files from ``self.files_py`` 
        """
        
        code_rst_file = DocumentationSphinxCodeRstFile(self.project_name, self.path_source, self.code_rst_header,
                                                       self.files_py, self.files_py_members, self.graph, self.o)
        code_rst_file.autorun()
    
    def add_additional_files_rst(self):
        """
        Copies additional rst-files (given in ``files.rst``) from ``path_files_rst`` to *'source/'*-folder.
        If rst-files already lie in source-folder no action is triggered.
        (*'code.rst'* is compulsory and is generated and no additional rst-file)
        """
        self.write("ADD additional rst-files")
        self.op()
        

        # test if rst-files already lie in source folder
        if self.path_files_rst == self.path_source:
            self.write("'path_files_rst' equals 'path_main/source' -> no copy necessary")
        
        # copy rst-files from 'path_files_rst' to 'path_main/source'
        else:
            if len(self.files_rst) > 1:  # more files than only code.rst
                self.write("copy rst-files from 'path_files_rst' to 'path_main/source'")
                self.op()
                
                for file_rst in self.files_rst:
                    if file_rst == 'code':
                        continue
                    self.write("copy rst-file '%s' from 'path_files_rst' to 'path_main/source'" % file_rst)
                    #~ cmd = 'xcopy %s %s /y' \
                               #~ % (adapt_string_for_dos(self.path_files_rst+'/'+file_rst+'.rst'), \
                                  #~ adapt_string_for_dos(self.path_source))                
                    #~ print cmd
                    #~ os.system()
                    src = os.path.join(self.path_files_rst,file_rst+'.rst')
                    dst = self.path_source
                    shutil.copy(src,dst)
                
                self.om()
        
        self.om()
        self.write("ADDING finished")
    
    def write_file_index_rst(self):
        """
        Write file *`index.rst`* via ``Documentation_sphinx_index_rst_file.autorun()``.
        Files in table-of-contents-tree are *'code.rst'* and additional rst-files
        """
        
        index_rst_file = Documentation_sphinx_index_rst_file(self.project_name, self.path_source, self.files_rst,  self.o)
        index_rst_file.autorun()
    
    def execute_command_line(self):
        """
        Executes command line to start sphinx's build of documentation:
        python <path_sphinx>/sphinx-build.py -b <output> [-d <path_doctree>] <path_source> <path_target> [> log.dat]
        
        e.g.::
        
            python "C:/Program Files (x86)/sphinx/sphinx-build.py" -b html 
                E:/tmp/source E:/tmp/build/html > E:/tmp/build/html/log.dat
        """
        self.write("EXECUTE command line")
        self.op()
        
        # - write basic command line
        #~ cmd = f"python {adapt_string_for_dos(self.path_sphinx)} -b {self.output}"
        #~ cmd = f"python {self.path_sphinx} -b {self.output]"
        cmd = f"{self.path_sphinx} -b {self.output}"
        
        # add additional options
        # - set verbose flag
        if self.path_doctree:
            #~ cmd = cmd + f" -d {adapt_string_for_dos(self.path_doctree)}"
            cmd = cmd + f" -d {self.path_doctree}"
        
        
        # add source and target destinations
        #~ cmd = cmd + f" {adapt_string_for_dos(self.path_source)} {adapt_string_for_dos(self.path_target)}"
        cmd = cmd + f" {self.path_source} {self.path_target}"
        
        
        # write log file if desired
        if self.log:
            if self.log == True:
                self.log = 'log.dat'
            
            self.write("set log-file to '%s'" % self.log)
            
            self.log = os.path.join(self.path_target,self.log)
            
            #~ self.log = adapt_string_for_dos(self.log)
            self.log = self.log
            
            cmd = cmd + ' > %s' % self.log
        
        # execute command line::
        #   python "C:\Program Files (x86)\sphinx\sphinx-build.py" <flag_x> <flagvalue_x> <source> <target>
        
        self.write("Execute command line: %s" % cmd)
        #~ ss
        os.system(cmd)
        
        self.om()
        self.write("EXECUTING finished")
    
    def delete_source_folder(self):
        """
        Deletes the *'source/'*-folder
        """
        self.write("DELETE source folder")
        self.op()
        
        # 2. delete source-folder
        #~ cmd = f"rmdir /q /s {adapt_string_for_dos(self.path_source)}"
        # cmd = f"rmdir {self.path_source}"
        #~ print cmd
        #~ os.system(cmd)
        shutil.rmtree(self.path_source)
        self.om()
        self.write("DELETING finished")
    
    
class DocumentationSphinxConfPyFile(BaseObject):
    """
    Class for the Sphinx configuration file *'conf.py'*.
    
    File consists of:
        1. Header
        2. General configuration
        3. Options for HTML output
        4. Options for LaTeX output
        5. Options for manual page output
        6. Options for Texinfo output
    
    Not all sections are necessary for every output.
    
    """
    def __init__(self, path_main, path_source, project_name, author, version, release, master_doc, path_graphviz,
                 output,  olvl=0):
        """
        The given parameters are assigned to attributes of the same name.
        
        :param path_main: Main path to the project to be documented. 
            The python-code-files to be documented are assumed here.
        :type path_main: string
        :param path_source: Source path of sphinx. Sphinx *'conf.py'* is written hereto 
        :type path_source: string
        :param project_name: Name of the software project to be documented. 
            Will appear multiple in documentation.
        :type project_name: string
        :param author: Author(s) of the software project.
        :type author: string
        :param version: Version of the software project.
        :type version: string
        :param release: Release of the software project.
        :type release: string
        :param master_doc: Name of the documentation master-file 
        :type master_doc: string
        :param path_graphviz: Path to *dot.exe* of program Graphviz. Necessary for inheritance diagrams.
        :type path_graphviz: string
        :param output: Output format. Common: *'html'*, *'singlehtml'*, *'Latex'*,... 
            (for more see sphinx documentation or -source-code)
        :type output: string
        :param olvl: Level of display output indentation. Handy if called by another instance.
        :type olvl: integer
        
        **Further possible parameters:**
        
        ==============================  ===============================================================================
        General configuration           needs_sphinx, extensions*, templates_path*, source_suffix*, source_encoding,
                                        master_doc*, version*, release*, language, today, today_fmt, exclude_patterns*, 
                                        default_role, add_function_parentheses, add_module_names, show_authors, 
                                        pygments_style*, modindex_common_prefix, keep_warnings
        Options for HTML output         html_theme*, html_style*, html_theme_options, html_theme_path, html_title, 
                                        html_short_title, html_logo*, html_favicon, html_static_path*, 
                                        html_last_updated_fmt, html_use_smartypants, html_sidebars, 
                                        html_additional_pages, html_domain_indices, html_use_index, html_split_index,
                                        html_show_sourcelink, html_show_sphinx, html_show_copyright, 
                                        html_use_opensearch, html_file_suffix, htmlhelp_basename*
        Options for LaTeX output        latex_elements*={'papersize','pointsize','preamble'},latex_documents*, 
                                        latex_logo, latex_use_parts, latex_show_pagerefs, latex_show_urls, 
                                        latex_appendices, latex_domain_indices
        Options for manual page output  man_pages*, man_show_urls
        Options for Texinfo output      texinfo_documents*, texinfo_appendices, texinfo_domain_indices, 
                                        texinfo_show_urls, texinfo_no_detailmenu
        ==============================  ===============================================================================
        
        * USED in default-template, others are umcommented

        
        """
        
        BaseObject.__init__(self)
        
        self.path_main = path_main
        self.path_source = path_source
        self.project_name = project_name
        self.author = author
        self.version = version
        self.release = release
        self.master_doc = master_doc
        self.path_graphviz = path_graphviz
        self.output = output  # necessary??? --> maybe later to reduce output in conf.py-file
        self.o = olvl
        
        
        self.f = None
        
        
    def autorun(self):
        """
        Write *'conf.py'* file to ``self.path_source``
        Not all sections are necessary for every output.
        
        =========================================  ============================
        1. write *header*                          (for all output)
        2. write *General configuration*           (for all output)
        3. write *Options for HTML output*         (for html output)
        4. write *Options for LaTeX output*        (for ouptut other than html)
        5. write *Options for manual page output*  (for ouptut other than html)
        6. write *Options for Texinfo output*      (for ouptut other than html)
        =========================================  ============================
        
        """
        
        self.write("WRITE conf.py-file with 'Documentation_sphinx_conf_py_file.autorun()'")
        
        self.open_file()
        
        self.write_header()
        self.write_general_configuration()
        if self.output in ['html', 'singlehtml']:
            self.write_options_for_html_output()
        else:
            self.write_options_for_latex_output()
            self.write_options_for_manual_page_output()
            self.write_options_for_texinfo_output()
        
        self.close_file()

        self.write("WRITING finished")
        
    def open_file(self):
        """
        Open the file ``self.path_source`` + *'/conf.py'* in mode *write*.
        """
        self.f = open(self.path_source + '/conf.py', 'w')  #: file *'conf.py'*
    
    def close_file(self):
        """
        Close file ``self.path_source`` + *'/conf.py'*
        """
        self.f.flush()
        self.f.close()
    
    def write_header(self):
        """
        Write *header* in file ``self.path_source`` + *'/conf.py'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("# -*- coding: utf-8 -*-\n\n")
        
        self.f.write("# %s documentation build configuration file, created by\n" % self.project_name)
        self.f.write("# class 'Documentation_sphinx_conf_py_file' methods")
        self.f.write("# probably called by 'Documatation_sphinx.write_file_conf_py'")
        self.f.write("# on %s.\n\n" % time.asctime())
        
        self.f.write("# This file is execfile()d with the current directory set to its containing dir.\n\n")
        
        self.f.write("# Note that not all possible configuration values are present in this\n")
        self.f.write("# autogenerated file.\n\n")
        
        self.f.write("# All configuration values have a default; values that are commented out\n")
        self.f.write("# serve to show the default.\n\n")
                
        self.f.write("import sys, os\n\n")
        
        self.f.write("# If extensions (or modules to document with autodoc) are in another directory,\n")
        self.f.write("# add these directories to sys.path here. If the directory is relative to the\n")
        self.f.write("# documentation root, use os.path.abspath to make it absolute, like shown here.\n")
        
        #~ self.f.write("sys.path.append(os.path.abspath('.'))\n")
        #~ self.f.write("sys.path.append(os.path.abspath('..'))\n")
        # - ODER -
        self.f.write("sys.path.append('%s')\n" % self.path_main)
        self.f.write("sys.path.append('%s')\n" % self.path_source)
    
    def write_general_configuration(self):
        """
        Write *General configuration* in file ``self.path_source`` + *'/conf.py'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("\n\n\n")
        self.f.write("# ------------------------------------------------------------------------------\n")
        self.f.write("# -- General configuration -----------------------------------------------------\n")
        self.f.write("# ------------------------------------------------------------------------------\n\n")
        
        self.f.write("# If your documentation needs a minimal Sphinx version, state it here.\n")
        self.f.write("#needs_sphinx = '1.0'\n\n")
        self.f.write("# Add any Sphinx extension module names here, as strings. They can be extensions\n")
        self.f.write("# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.\n")
        self.f.write("extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.coverage',"
                     "'sphinx.ext.pngmath', 'sphinx.ext.inheritance_diagram', 'sphinx.ext.autosummary',"
                     "'sphinx.ext.todo']\n\n")
        
        self.f.write("# Includes autosummary extension.\n")
        self.f.write("autosummary_generate = True\n\n")
        
        self.f.write("# Includes Todo extension.\n")
        self.f.write("todo_include_todos = True\n\n")
        
        self.f.write("# Add any paths that contain templates here, relative to this directory.\n")
        self.f.write("templates_path = ['_templates']\n\n")

        self.f.write("# The suffix of source filenames.\n")
        self.f.write("source_suffix = '.rst'\n\n")

        self.f.write("# The encoding of source files.\n")
        self.f.write("#source_encoding = 'utf-8-sig'\n\n")

        self.f.write("# The master toctree document.\n")
        self.f.write("master_doc = '%s'\n\n" % self.master_doc)

        self.f.write("# General information about the project.\n")
        self.f.write("project = u'%s'\n" % self.project_name)
        self.f.write("copyright = u'%s, %s'\n\n" % (time.localtime()[0],self.author) )

        self.f.write("# The version info for the project you're documenting, acts as replacement for\n")
        self.f.write("# |version| and |release|, also used in various other places throughout the\n")
        self.f.write("# built documents.\n")
        self.f.write("#\n")
        self.f.write("# The short X.Y version.\n")
        self.f.write("version = '%s'\n" % self.version)
        self.f.write("# The full version, including alpha/beta/rc tags.\n")
        self.f.write("release = '%s'\n\n" % self.release)

        self.f.write("# The language for content autogenerated by Sphinx. Refer to documentation\n")
        self.f.write("# for a list of supported languages.\n")
        self.f.write("#language = None\n\n")

        self.f.write("# There are two options for replacing |today|: either, you set today to some\n")
        self.f.write("# non-false value, then it is used:\n")
        self.f.write("#today = ''\n")
        self.f.write("# Else, today_fmt is used as the formaat for a strftime call.\n")
        self.f.write("#today_fmt = '%B %d, %Y'\n\n")

        self.f.write("# List of patterns, relative to source directory, that match files and\n")
        self.f.write("# directories to ignore when looking for source files.\n")
        self.f.write("exclude_patterns = []\n\n")

        self.f.write("# The reST default role (used for this markup: `text`) to use for all documents.\n")
        self.f.write("#default_role = None\n\n")

        self.f.write("# If true, '()' will be appended to :func: etc. cross-reference text.\n")
        self.f.write("#add_function_parentheses = True\n\n")

        self.f.write("# If true, the current module name will be prepended to all description\n")
        self.f.write("# unit titles (such as .. function::).\n")
        self.f.write("#add_module_names = True\n\n")

        self.f.write("# If true, sectionauthor and moduleauthor directives will be shown in the\n")
        self.f.write("# output. They are ignored by default.\n")
        self.f.write("#show_authors = False\n\n")

        self.f.write("# The name of the Pygments (syntax highlighting) style to use.\n")
        self.f.write("pygments_style = 'sphinx'\n\n")

        self.f.write("# A list of ignored prefixes for module index sorting.\n")
        self.f.write("#modindex_common_prefix = []\n\n")

        self.f.write('# If true, keep warnings as "system message" paragraphs in the built documents.\n')
        self.f.write("#keep_warnings = False\n\n")

        self.f.write("# The command name with which to invoke dot. The default is 'dot';\n")
        self.f.write("# You may need to set this to a full path if dot is not in the executable search path.\n")
        
        if platform.system()  == "Windows": # Graphviz path adaptation
            graphviz_path = self.path_graphviz.replace('/','\\\\')
            self.f.write(f"graphviz_dot='{graphviz_path}'\n")
        else:
            self.f.write(f"graphviz_dot='{self.path_graphviz}'\n")
    
    def write_options_for_html_output(self):
        """
        Write *Options for HTML output* in file ``self.path_source`` + *'/conf.py'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("\n\n\n")
        self.f.write("# ------------------------------------------------------------------------------\n")
        self.f.write("# -- Options for HTML output ---------------------------------------------------\n")
        self.f.write("# ------------------------------------------------------------------------------\n")

        self.f.write("# The theme to use for HTML and HTML Help pages.  See the documentation for\n")
        self.f.write("# a list of builtin themes.\n")
        self.f.write("html_theme = 'default'\n\n")

        self.f.write("html_style = 'ifls.css'\n\n")

        self.f.write("# Theme options are theme-specific and customize the look and feel of a theme\n")
        self.f.write("# further.  For a list of options available for each theme, see the\n")
        self.f.write("# documentation.\n")
        self.f.write("#html_theme_options = {}\n\n")

        self.f.write("# Add any paths that contain custom themes here, relative to this directory.\n")
        self.f.write("#html_theme_path = []\n\n")

        self.f.write("# The name for this set of Sphinx documents.  If None, it defaults to\n")
        self.f.write('# "<project> v<release> documentation".\n')
        self.f.write("#html_title = None\n\n")

        self.f.write("# A shorter title for the navigation bar.  Default is the same as html_title.\n")
        self.f.write("#html_short_title = None\n\n")

        self.f.write("# The name of an image file (relative to this directory) to place at the top\n")
        self.f.write("# of the sidebar.\n")
        self.f.write(f"html_logo = '{os.path.abspath(f"./_static/{IFL_LOGO_HTML}")}'\n\n")

        self.f.write("# The name of an image file (within the static path) to use as favicon of the\n")
        self.f.write("# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32\n")
        self.f.write("# pixels large.\n\n")
        self.f.write("#html_favicon = None\n\n")

        self.f.write("# Add any paths that contain custom static files (such as style sheets) here,\n")
        self.f.write("# relative to this directory. They are copied after the builtin static files,\n")
        self.f.write('# so a file named "default.css" will overwrite the builtin "default.css".\n')
        self.f.write("html_static_path = ['_static']\n\n")

        self.f.write("# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,\n")
        self.f.write("# using the given strftime format.\n")
        self.f.write("#html_last_updated_fmt = '%b %d, %Y'\n\n")

        self.f.write("# If true, SmartyPants will be used to convert quotes and dashes to\n")
        self.f.write("# typographically correct entities.\n")
        self.f.write("#html_use_smartypants = True\n\n")

        self.f.write("# Custom sidebar templates, maps document names to template names.\n")
        self.f.write("#html_sidebars = {}\n\n")

        self.f.write("# Additional templates that should be rendered to pages, maps page names to\n")
        self.f.write("# template names.\n")
        self.f.write("#html_additional_pages = {}\n\n")

        self.f.write("# If false, no module index is generated.\n")
        self.f.write("#html_domain_indices = True\n\n")

        self.f.write("# If false, no index is generated.\n")
        self.f.write("#html_use_index = True\n\n")

        self.f.write("# If true, the index is split into individual pages for each letter.\n")
        self.f.write("#html_split_index = False\n\n")

        self.f.write("# If true, links to the reST sources are added to the pages.\n")
        self.f.write("#html_show_sourcelink = True\n\n")

        self.f.write('# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.\n')
        self.f.write("#html_show_sphinx = True\n\n")

        self.f.write('# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.\n')
        self.f.write("#html_show_copyright = True\n\n")

        self.f.write("# If true, an OpenSearch description file will be output, and all pages will\n")
        self.f.write("# contain a <link> tag referring to it.  The value of this option must be the\n")
        self.f.write("# base URL from which the finished HTML is served.\n")
        self.f.write("#html_use_opensearch = ''\n\n")

        self.f.write('# This is the file name suffix for HTML files (e.g. ".xhtml").\n')
        self.f.write("#html_file_suffix = None\n\n")

        self.f.write("# Output file base name for HTML help builder.\n")
        self.f.write(f"htmlhelp_basename = '{self.project_name}s_doc'\n")
    
    def write_options_for_latex_output(self):
        """
        Write *Options for LaTeX output* in file ``self.path_source`` + *'/conf.py'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("\n\n\n")
        self.f.write("# ------------------------------------------------------------------------------\n")
        self.f.write("# -- Options for LaTeX output --------------------------------------------------\n")
        self.f.write("# ------------------------------------------------------------------------------\n")

        self.f.write("latex_elements = {\n")
        self.f.write("# The paper size ('letterpaper' or 'a4paper').\n")
        self.f.write("'papersize': 'a4paper',\n\n")
        self.f.write("# The font size ('10pt', '11pt' or '12pt').\n")
        self.f.write("#'pointsize': '10pt',\n\n")
        self.f.write("# Additional stuff for the LaTeX preamble.\n")
        self.f.write("#'preamble': '',\n")
        self.f.write("'footer': 'Institute of Aircraft Design \& Lightweight Structures (IFL), Technische Universitaet Braunschweig',\n")
        self.f.write("}\n\n")

        self.f.write("# Grouping the document tree into LaTeX files. List of tuples\n")
        self.f.write("# (source start file, target name, title, author, documentclass [howto/manual]).\n")
        self.f.write("latex_documents = [\n")
        # im zweiten String ist eigentlich im original vor dem unterstrich ein '\\' eingefuegt. notwendig?
        self.f.write("# ! WARNUNG: im zweiten String ist eigentlich im original vor einem unterstrich ein '\\' eingefuegt. notwendig? !\n")
        self.f.write(f"    ('{self.master_doc}', '{self.project_name}.tex', u'{self.project_name} Documentation',\n")
        self.f.write(f"     u'{self.author}', 'manual'),\n")
        self.f.write("]\n\n")

        self.f.write("# The name of an image file (relative to this directory) to place at the top of\n")
        self.f.write("# the title page.\n")
        #~ self.f.write("#latex_logo = None\n\n")        
        self.f.write(f"latex_logo = '{os.path.abspath(f"./_static/{IFL_LOGO_PDF}")}' \n\n")
        #~ 2010_Logo_IFL.png

        self.f.write('# For "manual" documents, if this is true, then toplevel headings are parts,\n')
        self.f.write("# not chapters.\n")
        self.f.write("#latex_use_parts = False\n\n")

        self.f.write("# If true, show page references after internal links.\n")     # good for printed docs
        self.f.write("latex_show_pagerefs = False\n\n")                            
        #~ self.f.write("latex_show_pagerefs = True\n\n")                            

        self.f.write("# If true, show URL addresses after external links.\n")
        #~ self.f.write("latex_show_urls = False\n\n")                            
        self.f.write("latex_show_urls = True\n\n")                            

        self.f.write("# Documents to append as an appendix to all manuals.\n")
        self.f.write("#latex_appendices = []\n\n")

        self.f.write("# If false, no module index is generated.\n")
        self.f.write("#latex_domain_indices = True\n")
            
    def write_options_for_manual_page_output(self):
        """
        Write *Options for manual page output* in file ``self.path_source`` + *'/conf.py'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("\n\n\n")
        self.f.write("# ------------------------------------------------------------------------------\n")
        self.f.write("# -- Options for manual page output --------------------------------------------\n")
        self.f.write("# ------------------------------------------------------------------------------\n")

        self.f.write("# One entry per manual page. List of tuples\n")
        self.f.write("# (source start file, name, description, authors, manual section).\n")
        self.f.write("man_pages = [\n")
        self.f.write(f"    ('{self.master_doc}', '{self.project_name}.tex', u'{self.project_name} Documentation',\n")
        self.f.write("     [u'SL'], 1)\n")
        self.f.write("]\n")

        self.f.write("# If true, show URL addresses after external links.\n")
        self.f.write("#man_show_urls = False\n")
    
    def write_options_for_texinfo_output(self):
        """
        Write *Options for Texinfo output* in file ``self.path_source`` + *'/conf.py'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("\n\n\n")
        self.f.write("# ------------------------------------------------------------------------------\n")
        self.f.write("# -- Options for Texinfo output ------------------------------------------------\n")
        self.f.write("# ------------------------------------------------------------------------------\n")

        self.f.write("# Grouping the document tree into Texinfo files. List of tuples\n")
        self.f.write("# (source start file, target name, title, author,\n")
        self.f.write("#  dir menu entry, description, category)\n")
        self.f.write("texinfo_documents = [\n")
        self.f.write(f"    ('{self.master_doc}', '{self.project_name}.tex', u'{self.project_name} Documentation',\n")
        self.f.write(f"   u'{self.author}', '{self.project_name}', 'One line description of project.',\n")
        self.f.write("   'Miscellaneous'),\n")
        self.f.write("]\n\n")

        self.f.write("# Documents to append as an appendix to all manuals.\n")
        self.f.write("#texinfo_appendices = []\n\n")

        self.f.write("# If false, no module index is generated.\n")
        self.f.write("#texinfo_domain_indices = True\n\n")

        self.f.write("# How to display URL addresses: 'footnote', 'no', or 'inline'.\n")
        self.f.write("#texinfo_show_urls = 'footnote'\n\n")

        self.f.write('# If true, do not generate a @detailmenu in the "Top" node\'s menu.\n')
        self.f.write("#texinfo_no_detailmenu = False\n\n")
        

class DocumentationSphinxCodeRstFile(BaseObject):
    """
    Class for the Sphinx code documentation file *'code.rst'*.
    
    File consists of:
    
    | 1. header
    |
    | For each python-file:
    | 2. headline
    | 3. ineritance diagram
    | 4. summary
    | 5. documentation
    
    The settings are used for all python files euqally.
    
    """
    
    def __init__(self, project_name, path_source, code_rst_header, files_py, files_py_members, graph, olvl=0):
        """
        The given parameters are assigned to attributes of the same name.
        
        :param project_name: Name of the software project to be documented. 
        :type project_name: string
        :param path_source: Source path of sphinx. Sphinx writes *'code.rst'* file hereto. Absolute path requiered.
        :type path_source: string
        :param code_rst_header: Header of the documentation. Written into 'code.rst'.
        :type code_rst_header: string
        :param files_py: List of strings with python file(s) with source code.
        :type files_py: list
        :param files_py_members: Gives for python source-code file(s) (=keys *(string)*)
            the members (classes, functions,...) (=values *(string,list of strings)*)
            that are to be included only in the documentation.
            All members are included if nothing else stated. 
        :type files_py_members: dict
        :param graph: Switch to include inheritance diagram. Graphiviz is necessary.
        :type graph: bool
        :param olvl: Level of display output indentation. Handy if called by another instance.
        :type olvl: integer
        """
        
        BaseObject.__init__(self)
        
        self.project_name = project_name
        self.path_source = path_source
        self.code_rst_header = code_rst_header
        self.files_py = files_py
        self.files_py_members = files_py_members
        self.graph = graph
        self.o = olvl
        
        self.f = None
        
    def autorun(self):
        """
        Write *'code.rst'* file to ``self.path_source``
        Not all sections are necessary for every output.
        
        | 1. write *header*
        |
        | For each python-file:
        | 2. write *headline*
        | 3. write *inheritance diagram*
        | 4. write *summary*
        | 5. write *documentation*
        
        """
        
        self.write("WRITE code.rst-file with 'Documentation_sphinx_code_rst_file.autorun()'")
        
        self.open_file()
        
        self.write_header()
        for python_file in self.files_py:
            self.write_headline(python_file)
            if self.graph:
                self.write_inheritance_diagram(python_file)
            self.write_summary(python_file)
            self.write_documentation(python_file)
        
        self.close_file()

        self.write("WRITING finished")
    
    def open_file(self):
        """
        Open the file ``self.path_source`` + *'/code.rst'* in mode *write*.
        """
        self.f = open(os.path.join(self.path_source,'code.rst'), 'w')
    
    def close_file(self):
        """
        Close file ``self.path_source`` + *'/code.rst'*
        """
        self.f.flush()
        self.f.close()
    
    def write_header(self):
        """
        Write *header* in file ``self.path_source`` + *'/code.rst'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write(f"{self.project_name}\n")
        
        l = len(self.project_name)
        self.f.write(f"{l*'='}\n\n")
        
        if self.code_rst_header:
            self.f.write(f"{self.code_rst_header}\n\n\n")
    
    def write_headline(self,python_file):
        """
        Write *headline* in file ``self.path_source`` + *'/code.rst'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write(f"Module {python_file}\n")
        
        l = len(python_file)
        self.f.write(f"{(7+l)*'"'}\n\n")
    
    def write_inheritance_diagram(self, python_file):
        """
        Write *inheritance diagram* in file ``self.path_source`` + *'/code.rst'*.
        File must be already opened with ``self.open_file()``
        
        .. Note::            
            deactivated the line .. xmodule::
        
        
        """
        self.f.write("Inheritance diagram\n###################\n\n")
        #~ self.f.write(".. xmodule::  %s\n\
        self.f.write(".. inheritance-diagram::  %s\n\n" % python_file)
        self.f.write("---------\n\n")
    
    def write_summary(self,python_file):
        """
        Write *summary* in file ``self.path_source`` + *'/code.rst'*.
        File must be already opened with ``self.open_file()``
        
        .. Note::
        ::
            deactivated the line :toctree: after .. autosummary::
        
        .. Note::
            Autosummary directive only works when members are indicated directly in code.rst as shown below.
            As the autoamtic generation does not work at the moment (v.1.1.3) the members are added here by importing the modules and searching for entries.
        
        .. code-block:: console
        
            Summary

            .. currentmodule:: PyNastranOptimizer

            .. autosummary::  
               :toctree: .    
                
               Optimizer
               Optimizer.__init__
               Optimizer.setSolverParameters
            
        
            Module PyNastranOptimizer
            """""""""""""""""""""""""
        
        .. code-block:: console
            
            Inheritance diagram
            ######################

            .. inheritance-diagram::  PyNastranOptimizer


            **Summary**
            ###########

            .. currentmodule:: PyNastranOptimizer

            class members
            *****************

            .. autosummary::     
               :toctree:


                Optimizer    

            module functions
            ***********

            .. autosummary::     
               :toctree:

                afunctiondummy
                
            Detailed Description
            ########################

            .. automodule::  PyNastranOptimizer
               :members:
               :special-members:
               :undoc-members:
               :show-inheritance:
        """
        
        
        #
        import inspect        
        module = __import__(str(python_file))
        
        class_dict = {}
        function_list = []
        
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                #~ print "We have a class:",obj
                if str(obj).startswith(str(python_file)):
                    print ('#'*40)
                    print ('--Class "%s" is of our module "%s".' % (obj,python_file))
                    
                    classtree = inspect.getclasstree([obj])
                    print ("classtree",classtree)
                    for class_obj in classtree:
                        print( '-',class_obj)
                        
                        if isinstance(class_obj,list):
                            class_obj = class_obj[0]
                        if class_obj[0] not in class_dict:
                            class_dict[class_obj[0]] = []
                        memberdictionary = class_obj[0].__dict__
                        print (class_obj[0],"dict",memberdictionary)
                        
                        for member in memberdictionary:
                            print( member)
                            if member not in class_dict[class_obj[0]]:
                                
                                class_dict[class_obj[0]].append(member)
                    
                    
            if inspect.ismethod(obj):
                print( '--METHOD',obj)
                
            if inspect.isfunction(obj):
                print( '--FUNCTION',obj                )
                function_list.append(str(obj).split()[1])
        
        
        
        self.f.write("Summary\n#########\n\n")
        self.f.write(".. currentmodule::  %s\n\n" % python_file)
        # members here
        if len(class_dict)>0:
            self.f.write("Classes and members\n*******************\n\n")        
            
            self.f.write(".. autosummary::\n")
            self.f.write("   :toctree:\n\n")        
            for class_name in class_dict:
                try:
                    modulename = class_name.split('.')[0]
                    class_name_wo_module = str(class_name).split(modulename+".")[1]
                except Exception as e:
                    print (e)
                    class_name_wo_module = str(class_name)
                self.f.write(f"   {class_name_wo_module}\n")
                member_list = class_dict[class_name]
                for member in sorted(member_list):
                    if not member.startswith("__doc__"): #skip the __doc__ member
                        joined_string = '.'.join([class_name_wo_module,member])
                        self.f.write(f"   {joined_string}\n")
        
        self.f.write("\n")
        
        # functions here
        if len(function_list)>0:
            self.f.write("Module functions\n*******************\n\n")        
            self.f.write(".. autosummary::\n")
            self.f.write("   :toctree:\n\n")            
            for function in function_list:
                self.f.write(f"   {function}\n")
        
        self.f.write("\n")
        #~ self.f.write("---------\n\n")
        
        return
    
    def write_documentation(self,python_file):
        """
        Write *documentation* in file ``self.path_source`` + *'/code.rst'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("Detailed Description\n####################\n\n")
        
        self.f.write(".. automodule::  %s\n" % python_file)
        if python_file in self.files_py_members:
            self.f.write("   :members: %s\n" % ', '.join(self.files_py_members[python_file]))
        else:
            self.f.write("   :members:\n")
        # private members can also be included into the documentation
        # self.f.write("   :private-members:\n")
        if sphinx_version >= '1.1':
            self.f.write("   :special-members:\n")
        #
        self.f.write("   :undoc-members:\n")
        self.f.write("   :show-inheritance:\n\n\n")
        

class Documentation_sphinx_index_rst_file(BaseObject):
    """
    Class for the Sphinx code index file *'index.rst'*.
    
    File consists of:
        1. header
        2. headline
        3. contents
        4. indices and tables
    
    """
    
    def __init__(self, project_name, path_source, files_rst, olvl=0):
        """
        The given parameters are assigned to attributes of the same name.
        
        :param project_name: Name of the software project to be documented.
        :type project_name: string
        :param path_source: Source path of sphinx. Sphinx writes *'code.rst'* file hereto. Absolute path requiered.
        :type path_source: string
        :param files_rst: List of strings of additional rst-files. Inclusion into documentation is in order of appearance in list.
            *'code.rst'* must be included.
        :type files_rst: list
        :param olvl: Level of display output indentation. Handy if called by another instance.
        :type olvl: integer
        """
        
        BaseObject.__init__(self)
        
        self.project_name = project_name
        self.path_source = path_source
        self.files_rst = files_rst
        self.o = olvl

        self.f = None
        
    
    def autorun(self):
        """
        Write *'index.rst'* file to ``self.path_source``
        
        1. write *header*
        2. write *headline*
        3. write *contents*
        4. write *indices and tables*
        
        """
        
        self.write("WRITE index.rst-file with 'Documentation_sphinx_index_rst_file.autorun()'")
        
        self.open_file()
        
        self.write_header()
        self.write_headline()
        self.write_contents()
        self.write_indices_and_tables()
        
        self.close_file()

        self.write("WRITING finished")
    
    def open_file(self):
        """
        Open the file ``self.path_source`` + *'/index.rst'* in mode *write*.
        """
        self.f = open(os.path.join(self.path_source,'index.rst'), 'w')
    
    def close_file(self):
        """
        Close file ``self.path_source`` + *'/index.rst'*
        """
        self.f.flush()
        self.f.close()
    
    def write_header(self):
        """
        Write *header* in file ``self.path_source`` + *'/index.rst'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write(".. %s documentation master file, created by\n" % self.project_name)
        self.f.write("   class 'Documentation_sphinx_index_rst_file' methods\n")
        self.f.write("   probably called by 'Documatation_sphinx.write_file_index_rst'\n")
        self.f.write("   on %s.\n" % time.asctime())
        self.f.write("   You can adapt this file completely to your liking, but it should at least\n")
        self.f.write("   contain the root `toctree` directive.\n")
    
    def write_headline(self):
        """
        Write *headline* in file ``self.path_source`` + *'/index.rst'*.
        File must be already opened with ``self.open_file()``
        """
        
        headline = "\nWelcome to %s's documentation!\n" % self.project_name
        self.f.write(headline)
        self.f.write("%s\n\n" % ((len(headline)-2)*'='))
    
    def write_contents(self):
        """
        Write *contents* in file ``self.path_source`` + *'/index.rst'*.
        File must be already opened with ``self.open_file()``
        """
        
        #~ self.f.write("Contents:\n\n")
        self.f.write(".. toctree::\n")
        self.f.write("   :maxdepth: 4\n\n")
        
        for file_rst in self.files_rst:
            self.f.write("   %s\n" % file_rst)
        self.f.write("\n")
    
    def write_indices_and_tables(self):
        """
        Write *indices and tables* in file ``self.path_source`` + *'/index.rst'*.
        File must be already opened with ``self.open_file()``
        """
        
        self.f.write("\nIndices and tables\n")
        self.f.write("%s\n\n" % (18*'='))
        self.f.write("* :ref:`genindex`\n")
        self.f.write("* :ref:`modindex`\n")
        self.f.write("* :ref:`search`\n")
        


#
if __name__ == '__main__':
    main()

