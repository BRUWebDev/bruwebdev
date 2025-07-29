import { Modal } from "bootstrap";

/* eslint-disable no-unused-vars */
function openPortfolioModal(url) {
  const portfolioModal = new Modal("#modal-portfolio", {
    keyboard: false,
  });
  const portfolioPreview = document.getElementById("portfolio-preview");
  portfolioPreview.setAttribute("src", url);
  portfolioModal.show();
}
