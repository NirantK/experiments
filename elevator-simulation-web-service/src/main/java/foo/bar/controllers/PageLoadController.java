package foo.bar.controllers;

import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.method.support.ModelAndViewContainer;

/**
 * Created by jainpj on 18/02/17.
 */
@Path("/")
public class PageLoadController {

    @GET
    @Produces(MediaType.TEXT_HTML)

    public String loadPage(){

        return "<html> <title>Hack Kone</title>\n"
                + "<script type=\"application/javascript\" src=\"js/abc.js\"></script>\n"
                + "<script type='application/javascript' src='https://ajax.googleapis"
                + ".com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>\n"
                + "<body>\n"
                + "Test\n"
                + "<div id=\"abc\"></div>\n"
                + "</body>\n"
                + "</html> ";
    }
}
