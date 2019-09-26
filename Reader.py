import codecs
import re

import docx
import docx.document
import docx.oxml.table
import docx.oxml.text.paragraph
import docx.table
import docx.text.paragraph
import pandas as pd


class Reader(object):
    @classmethod
    def get_reader(cls, ext_name):
        if ext_name == 'docx':
            return DocxReader()
        elif ext_name == 'xlsx':
            return XlsxReader()
        elif ext_name == 'txt':
            return TxtReader()
        else:
            return NullReader()

    def read(self, file_name):
        raise Exception("non implement read.")



class DocxReader(Reader):
    def iter_paragraphs(self, parent, recursive=True):
        """
        Yield each paragraph and table child within *parent*, in document order.
        Each returned value is an instance of Paragraph. *parent*
        would most commonly be a reference to a main Document object, but
        also works for a _Cell object, which itself can contain paragraphs and tables.
        """
        if isinstance(parent, docx.document.Document):
            parent_elm = parent.element.body
        elif isinstance(parent, docx.table._Cell):
            parent_elm = parent._tc
        else:
            raise TypeError(repr(type(parent)))

        for child in parent_elm.iterchildren():
            if isinstance(child, docx.oxml.text.paragraph.CT_P):
                yield docx.text.paragraph.Paragraph(child, parent)
            elif isinstance(child, docx.oxml.table.CT_Tbl):
                if recursive:
                    table = docx.table.Table(child, parent)
                    for row in table.rows:
                        for cell in row.cells:
                            for child_paragraph in self.iter_paragraphs(cell):
                                yield child_paragraph

    def read(self, file_name):
        fullText = []
        document = docx.Document(file_name)
        for paragraph in self.iter_paragraphs(document):
            fullText.append(paragraph.text)
        return '\n'.join(fullText) + '\n'


class XlsxReader(Reader):
    def read(self, file_name):
        fullText = ""
        sheet_data = pd.read_excel(file_name, index_col=None, header=None, keep_default_na=False, sheet_name=None)
        for sheet in sheet_data.values():
            fullText += sheet.to_string()
            fullText = re.sub(r"\n\d+", "", fullText)
        return fullText + '\n'

class TxtReader(Reader):
    def read(self, file_name):
        content = '\n'.join([line.strip()
                             for line in codecs.open(file_name, 'r', 'utf-8')
                             if len(line.strip()) > 0])
        return content


class NullReader(Reader):
    def read(self, file_name):
        return ""
